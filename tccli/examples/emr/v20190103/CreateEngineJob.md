**Example 1: 创建周期性任务**

创建周期性任务

Input: 

```
tccli emr CreateEngineJob --cli-unfold-argument  \
    --InstanceId emr-3x4a7b6u \
    --JobType notebook \
    --JobContent /workspace/999/ttt.ipynb \
    --JobUUID test_user_3 \
    --ExecuteUser test_user \
    --Parameters.0.Name KERNEL_TYPE \
    --Parameters.0.Value PySpark \
    --ExtParameters.0.Name spark.yarn.queue \
    --ExtParameters.0.Value default \
    --ExecutePassword asdasfa \
    --ResourcePath /a/b/c
```

Output: 
```
{
    "Response": {
        "EngineJobId": "139",
        "RequestId": "4ef63fc5-b02e-4cd0-9bf4-5c98a432d4b1"
    }
}
```

