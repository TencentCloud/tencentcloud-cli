**Example 1: 创建mongodb kill 任务示例**

创建kill任务

Input: 

```
tccli dbbrain CreateMongoDBKillTask --cli-unfold-argument  \
    --InstanceId cmgo-841j039d \
    --Duration 123 \
    --Product mongodb \
    --Time 12
```

Output: 
```
{
    "Response": {
        "RequestId": "0a3a18e5-f4f9-4c2e-82a6-e16ddd186af9",
        "Status": 1
    }
}
```

