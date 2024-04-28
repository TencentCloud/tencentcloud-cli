**Example 1: 创建并执行Spark SQL批任务**

本接口（CreateSparkSessionBatchSQL）用于向Spark作业引擎提交Spark SQL批任务

Input: 

```
tccli dlc CreateSparkSessionBatchSQL --cli-unfold-argument  \
    --DataEngineName data_engine_1 \
    --ExecuteSQL c2VsZWN0IDE= \
    --DriverSize small \
    --ExecutorSize small \
    --ExecutorNumbers 1 \
    --ExecutorMaxNumbers 1 \
    --TimeoutInSecond 2 \
    --SessionId  \
    --SessionName livy-session-123 \
    --Arguments.0.Value eni \
    --Arguments.0.Key test_eni
```

Output: 
```
{
    "Response": {
        "BatchId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
        "Statements": [
            {
                "TaskId": "098923ea-d6c0-4cd9-bbed-2e90c9cf04dc",
                "SQL": "select 1;"
            }
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

