import mlflow

# 开启一次实验运行
with mlflow.start_run():
    # 记录超参（参数名，参数值）
    mlflow.log_param("parameter name", "value")
    # 记录评估指标（指标名，数值）
    mlflow.log_metric("metric name", 1)
    # 在这里写训练模型、保存模型、注册模型代码
