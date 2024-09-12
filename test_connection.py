import mlflow

def test_mlflow_connection():
    mlflow.set_tracking_uri("http://localhost:5000")
    runs = mlflow.search_runs()
    print(runs)

if __name__ == "__main__":
    test_mlflow_connection()
