import dagshub
import mlflow

# 连接DagsHub远程仓库
dagshub.init(repo_owner="raynawtw", repo_name="my-mlflow-project", mlflow=True)

# 开启一次MLflow实验运行
with mlflow.start_run():
    mlflow.log_param("parameter name", "value")
    mlflow.log_metric("metric name", 1)
