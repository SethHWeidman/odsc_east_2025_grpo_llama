import math

from scipy import stats
from scipy.stats import norm


def compare_proportions_independent_samples(
    successes1: int, n1: int, successes2: int, n2: int, alpha: float = 0.05
) -> float:
    """
    Perform a two-proportion z-test to compare proportions between two samples.

    Parameters:
    - successes1 (int): Number of successes in the first sample.
    - n1 (int): Size of the first sample.
    - successes2 (int): Number of successes in the second sample.
    - n2 (int): Size of the second sample.
    - alpha (float): Significance level (default is 0.05).

    Returns:
    - float: The p-value from the two-proportion z-test.
    """
    # Input validation
    if not (0 <= successes1 <= n1 and 0 <= successes2 <= n2):
        raise ValueError("Successes must be between 0 and sample size.")
    if n1 <= 0 or n2 <= 0:
        raise ValueError("Sample sizes must be positive.")

    # Calculate proportions
    p1 = successes1 / n1
    p2 = successes2 / n2

    # Calculate pooled proportion
    p_hat = (successes1 + successes2) / (n1 + n2)

    # Calculate standard error
    se = math.sqrt(p_hat * (1 - p_hat) * (1 / n1 + 1 / n2))

    # Calculate z-statistic
    z = (p1 - p2) / se

    # Calculate two-tailed p-value
    p_value = 2 * (1 - norm.cdf(abs(z)))

    # Display results
    print(f"z-value: {z:.4f}")
    if p_value < alpha:
        print(f"The difference is statistically significant at the {alpha} level.")
    else:
        print(f"The difference is not statistically significant at the {alpha} level.")

    return p_value


def check_significance_proportions_difference(
    sample1: list[float], sample2: list[float], alpha: float = 0.05
) -> float:
    """
    Perform Welch's t-test on two samples and check for statistical significance.

    Parameters:
    - sample1 (list of float): First sample of 20 floats.
    - sample2 (list of float): Second sample of 20 floats.
    - alpha (float): Significance level (default is 0.05).

    Returns:
    - float: The p-value from Welch's t-test.
    """
    # Check if both samples have exactly 20 elements
    if len(sample1) != 20 or len(sample2) != 20:
        raise ValueError("Both samples must have exactly 20 elements.")

    # Perform Welch's t-test
    stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

    # Display the results
    print(f"T-statistic: {stat:.4f}")
    if p_value < alpha:
        print(f"The difference is statistically significant at the {alpha} level.")
    else:
        print(f"The difference is not statistically significant at the {alpha} level.")

    return p_value


if __name__ == "__main__":
    pre_train_sample_20_questions = [
        1,
        5,
        5,
        3,
        5,
        3,
        5,
        2,
        5,
        1,
        5,
        5,
        5,
        0,
        2,
        4,
        4,
        4,
        4,
        5,
    ]

    post_train_sample_20_questions = [
        5,
        5,
        5,
        4,
        5,
        5,
        4,
        5,
        5,
        2,
        5,
        5,
        5,
        5,
        4,
        5,
        5,
        4,
        4,
        5,
    ]
    print(sum(pre_train_sample_20_questions))
    print(sum(post_train_sample_20_questions))

    p_value_1 = compare_proportions_independent_samples(
        sum(pre_train_sample_20_questions),
        5 * 20,
        sum(post_train_sample_20_questions),
        5 * 20,
    )
    print(f"p-value: {p_value_1:.4f}")
    print()

    p_value_2 = check_significance_proportions_difference(
        [prop / 5.0 for prop in pre_train_sample_20_questions],
        [prop / 5.0 for prop in post_train_sample_20_questions],
    )
    print(f"p-value: {p_value_2:.4f}")
