"""Praktikum 3 - Polymorphism & Duck Typing: Evaluator Model ML."""
import math


class RegressionModel:
    def evaluate_performance(self, x_test, y_test) -> dict:
        """x_test = prediksi model, y_test = nilai aktual -> MSE & RMSE."""
        n = len(y_test)
        mse = sum((a - p) ** 2 for a, p in zip(y_test, x_test)) / n
        return {"model": "Regression", "MSE": round(mse, 4),
                "RMSE": round(math.sqrt(mse), 4)}


class ClassificationModel:
    def evaluate_performance(self, x_test, y_test) -> dict:
        """x_test = label prediksi, y_test = label aktual -> Accuracy."""
        benar = sum(1 for a, p in zip(y_test, x_test) if a == p)
        return {"model": "Classification",
                "Accuracy": round(benar / len(y_test), 4)}


class ClusteringModel:
    def evaluate_performance(self, x_test, y_test) -> dict:
        """x_test = titik data (1D), y_test = label klaster -> Silhouette."""
        def dist(a, b):
            return abs(a - b)
        scores = []
        for i, (xi, li) in enumerate(zip(x_test, y_test)):
            same = [dist(xi, xj) for j, (xj, lj) in enumerate(zip(x_test, y_test))
                    if lj == li and j != i]
            a = sum(same) / len(same) if same else 0.0
            b = min(
                sum(dist(xi, xj) for xj, lj in zip(x_test, y_test) if lj == c)
                / sum(1 for lj in y_test if lj == c)
                for c in set(y_test) if c != li
            )
            scores.append((b - a) / max(a, b) if max(a, b) else 0.0)
        return {"model": "Clustering",
                "Silhouette Score": round(sum(scores) / len(scores), 4)}


def run_model_evaluation(model_instance, x_data, y_data) -> dict:
    """Duck typing: cukup punya evaluate_performance()."""
    hasil = model_instance.evaluate_performance(x_data, y_data)
    print(f"=== Evaluasi {hasil['model']} ===")
    for k, v in hasil.items():
        if k != "model":
            print(f"  {k}: {v}")
    return hasil


if __name__ == "__main__":
    run_model_evaluation(RegressionModel(),
                         [2.8, 5.1, 7.2, 8.9], [3.0, 5.0, 7.0, 9.0])
    run_model_evaluation(ClassificationModel(),
                         [1, 0, 1, 1, 0], [1, 0, 0, 1, 0])
    run_model_evaluation(ClusteringModel(),
                         [1.0, 1.2, 0.8, 8.0, 8.3, 7.9], [0, 0, 0, 1, 1, 1])

    class DummyModel:  # tanpa pewarisan, tetap diterima
        def evaluate_performance(self, x, y):
            return {"model": "Dummy", "Skor": 1.0}
    run_model_evaluation(DummyModel(), [], [])
