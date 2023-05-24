**Example 1: 提交Spark SQL批任务**

提交Spark SQL批任务

Input: 

```
tccli dlc CreateSparkSessionBatchSQL --cli-unfold-argument  \
    --DataEngineName data_engine_1 \
    --ExecuteSQL select 1 \
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
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "BatchId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742"
    }
}
```

