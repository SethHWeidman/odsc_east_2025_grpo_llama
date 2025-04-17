# Fine-tuning Llama, using GRPO and LoRa, on a single A100.

This repo illustrates how to use "industry-standard" libraries - all of which happen to be from the [HuggingFace](https://huggingface.co) stack:

* [transformers](https://github.com/huggingface/transformers)
* [datasets](https://github.com/huggingface/datasets)
* [peft](https://github.com/huggingface/peft)
* [trl](https://github.com/huggingface/trl)

To:

* Download the [8B parameter Llama3.1 model](https://ai.meta.com/blog/meta-llama-3-1/).
* Add [LoRa](https://arxiv.org/abs/2106.09685) adapters to the model.
* Read in the [GSM8K dataset](https://openai.com/index/solving-math-word-problems/) frop OpenAI.
* Fine-tuning the model's LoRa adapters using GRPO, introduced by DeepSeek in their [DeepSeekMath](https://arxiv.org/pdf/2402.03300) paper.

all on a single A100 GPU!