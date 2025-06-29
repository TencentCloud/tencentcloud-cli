**Example 1: 成功示例**

成功示例

Input: 

```
tccli apm CreateProfileTask --cli-unfold-argument  \
    --ServiceName springboot-service \
    --InstanceId apm-ewyzCXlxj \
    --ServiceInstance 127.0.0.1 \
    --StartTime 0 \
    --Duration 5000 \
    --Event cpu \
    --AllTimes 1 \
    --TaskInterval 10000
```

Output: 
```
{
    "Response": {
        "RequestId": "eac7cf53-1900-4367-9076-a5649ddd4dbb",
        "TaskId": 10001
    }
}
```

