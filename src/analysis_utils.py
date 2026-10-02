import pandas as pd


def load_data(file_path):
    """读取成绩数据"""
    return pd.read_csv(file_path)


def calculate_scores(df):
    """计算总分"""
    df["total"] = (
        df["listening"]
        + df["reading"]
        + df["writing"]
    )

    return df


def analyze_scores(df):
    """分析成绩"""

    subject_avg = {
        "听力": df["listening"].mean(),
        "阅读": df["reading"].mean(),
        "写作": df["writing"].mean()
    }

    return {
        "exam_count": len(df),
        "average_total": df["total"].mean(),
        "max_total": df["total"].max(),
        "best_subject": max(
            subject_avg,
            key=subject_avg.get
        ),
        "worst_subject": min(
            subject_avg,
            key=subject_avg.get
        ),
        "subject_avg": subject_avg
    }