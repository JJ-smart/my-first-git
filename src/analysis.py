import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from analysis_utils import (
    load_data,
    calculate_scores,
    analyze_scores
)


def print_report(result):
    """打印分析结果"""

    print("===== CET-6 成绩分析 =====")

    print(f"考试次数：{result['exam_count']}")
    print(f"平均总分：{result['average_total']:.1f}")
    print(f"最高总分：{result['max_total']}")

    print("\n===== 各科平均分 =====")

    for subject, score in result["subject_avg"].items():
        print(f"{subject}：{score:.1f}")

    print(f"\n表现最好：{result['best_subject']}")
    print(f"表现最弱：{result['worst_subject']}")


def plot_scores(df):
    """绘制总分趋势图"""
    plt.figure(figsize=(8, 5))

    plt.plot(
        df["date"],
        df["total"],
        marker="o",
        label="Total"
    )

    plt.title("CET-6 Total Score Trend")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)

    plt.savefig("data/score_trend.png")
    plt.close()

    print("成绩趋势图已保存：data/score_trend.png")

def main():
    df = load_data("data/scores.csv")

    df = calculate_scores(df)

    result = analyze_scores(df)

    print_report(result)

    plot_scores(df)


if __name__ == "__main__":
    main()