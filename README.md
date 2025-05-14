# Fine-tuning Llama, using GRPO and LoRa, on a single A100.

This repo illustrates how to use "industry-standard" libraries - all of which happen to be from the
[HuggingFace](https://huggingface.co) stack:

- [transformers](https://github.com/huggingface/transformers)
- [datasets](https://github.com/huggingface/datasets)
- [peft](https://github.com/huggingface/peft)
- [trl](https://github.com/huggingface/trl)

To:

- Download the [8B parameter Llama3.1 model](https://ai.meta.com/blog/meta-llama-3-1/).
- Add [LoRa](https://arxiv.org/abs/2106.09685) adapters to the model.
- Read in the [GSM8K dataset](https://openai.com/index/solving-math-word-problems/) frop OpenAI.
- Fine-tuning the model's LoRa adapters using GRPO, introduced by DeepSeek in their
  [DeepSeekMath](https://arxiv.org/pdf/2402.03300) paper.

all on a single A100 GPU!

![Proportion Plot](https://data-science-talks.s3.us-east-1.amazonaws.com/odsc_east_2025/images/proportion_plot.png)

## Innovations

There are other repos and tutorials showing how to use the libraries from the `transformers`
ecosystem. **The difference with this repo is that we put the pieces together in a way that
actually works**:

- Before adding LoRa adapters and fine-tuning, upon manual inspection, the model gets **72 or 73**
  out of 100 answers right from the dataset.
- After adding the LoRa adapters, and training them in Google Colab (including lots of tips on how
  to do this, see below), the model gets **92** out of 100 answers correct!

### Statistical significance

How do we know the fine-tuning process really did produce a model that "learned", as opposed to one
that just did slightly better by chance? I'll briefly discuss how I arrived at the "73" and "92"
numbers above and the tests I ran to determine if the difference was significant.

The sample size of 100 comes from randomly sampling 20 cases from the test set, generating five
answers for each one, and manually inspecting each answer to confirm whether it was correct (if the
model outputted "$15" when the correct answer was "15", I counted it as correct). This leads
to a small amount of ambiguity in the estimates, since in a small amount of cases (just one of the
100 answers observed) it was ambiguous whether the model's generated answer was correct. Even
taking the more "conservative" case - counting a "borderline" answer from the pre-trained model as
correct - fine-tuning does indeed result in a statistically signficant improvement in model
performance (p-value of 0.0004).

Furthermore, even considering a much more conservative test - one that treats these as just 20
observations, each one having a `float` value from 0.0 to 1.0 - produces a p-value of 0.0256.

![Proportion Plot](https://data-science-talks.s3.us-east-1.amazonaws.com/odsc_east_2025/images/proportions_difference_plot.png)

Since these 20 observations were chosen randomly from the test set I conclude that the fine-tuning
process - despite only running through 800 examples, see "[Early stopping](#early-stopping)" below
\- did in fact make the model better at answering questions from the GSM8K dataset. See
`stats_tests.py` for the details.

## Learnings related to getting the training to work

There were two entirely different kinds of learnings: around the reward functions, and the coding
environment. The coding environment learnings are encapsulated in a set of helper functions that
are mostly in the `2-ODSC_East_2025_GRPO_on_Llama-Training.ipynb` notebook.

### Reward functions

Reward functions matter for GRPO, and tweaking them took some trial and error. Plugging in naive
reward functions you can find in other tutorials resulted in the model producing degenerate outputs
that fit a specified output format but don't have meaningful content (won't call out any one in
particular, but you can find what I'm referring to through Googling). Some reward function
combinations allowed the model to simply More generally, many reward functions seemed to result in
the model producing answers that were too short to meaningfully reason through the problem.

The key for this experiment ended up being to incentize getting the answer right strongly, but
contingent on the answer being sufficiently long. I ended up giving a reward of `5.0` for the
correct answer, with a penalty for answers less than 100 tokens, and an automatic `0.0` for any
answer less than 50 tokens. The model could only earn up to `1.5` for formatting the answer
correctly.

### Early stopping

While GRPO has many plusses as a fine-tuning algorithm, recent blog posts confirm its instability.
My experience confirms this: while training, and calculating the loss every 25 steps, the loss
shoots up around step 1,200, and increases thereafter! For evaluating the final fine-tuned model, I
used the model trained for only 800 steps--which, since `per_device_train_batch_size=6` (and I only
used one GPU), `gradient_accumulation_steps=4`, and `num_generations=6`, means the model only saw
`800 * 6 * 4 / 6 = 3200` total examples during training!

![Training loss plot](https://data-science-talks.s3.us-east-1.amazonaws.com/odsc_east_2025/images/training_loss_plot.png)

### Coding environment

There were many learnings related to getting training, which took on the order of ~24 hours total
on a single A100, to work in a Google Colab environment where exiting your browser clears the
memory of your session. The `Training` notebook saves the training run to S3 every 25 training
steps, optionally restarting training from a previously-saved-on-S3 checkpoint, and the
`Fine-Tune-Results` notebook reads in an S3 checkpoint for downstream use.

## The four notebooks

There are four notebooks that accomplish different parts of this. Each notebook can be run
start-to-finish on a Google Colab instance with a single A100 GPU. Note that in order to use A100
GPUs, you may need to sign up for a $9.99/month Google Colab Pro subscription.

1. `1-ODSC_East_2025_GRPO_on_Llama-Baseline.ipynb` shows how to:

- Load in the baseline ~8B parameter Llama 3.1 model
- Load in the GSM8K dataset
- Generate responses using the baseline model, saving the results to S3 along the way

2. `2-ODSC_East_2025_GRPO_on_Llama-Training.ipynb` shows how to:

- Load in the baseline ~8B parameter Llama 3.1 model
- Load in the GSM8K dataset
- Add LoRa adapters to the model
- Set up GRPO training for this model and dataset, including specifying the reward functions
- Add a callback to training that saves the checkpointed model to S3 every 25 training steps
- Also log the rewards in the notebook every 25 steps
- Train the model, optionally restarting training from one of the checkpoints

3. `3-ODSC_East_2025_GRPO_on_Llama-Fine-Tune-Results.ipynb` shows how to:

- Load in the baseline ~8B parameter Llama 3.1 model
- Load in the GSM8K dataset
- Load in one of the training checkpoints and re-evaluate the model with the trained LoRa adapters

4. Finally, `4_ODSC_East_2025_GRPO_on_Llama-Compare-Results.ipynb` shows how to compare the results
   of two model variants. This was used to evaluate the results pre-and-post fine-tuning.

# Swap ins and outs

[Swap-ins-and-outs](swap_ins_and_outs.md) contains example questions that the post-fine
tuning model answered correctly that the pre-fine tuning model did not, and vice versa, as well as
questions that both models answered correctly or incorrectly for comparison.
