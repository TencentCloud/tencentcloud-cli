**Example 1: 修改mongoDB实例参数**

用户发起修改其mongoDB的参数配置

Input: 

```
tccli mongodb ModifyInstanceParams --cli-unfold-argument  \
    --InstanceId cmgo-9d0p6umb \
    --InstanceParams.0.Value operation.profiling.slowOpThresholdMs \
    --InstanceParams.0.Key operation.profiling.slowOpThresholdMs
```

Output: 
```
{
    "Response": {
        "Changed": true,
        "RequestId": "e51b4590-db7b-4835-9899-1f5c33f92fbf",
        "TaskId": 0
    }
}
```

