**Example 1: 生产消费延迟**

生产消费延迟

Input: 

```
tccli ckafka DelayMessage --cli-unfold-argument  \
    --InstanceId abc \
    --AccessPoint 127.0.0.1:9092 \
    --DelayDuration 60
```

Output: 
```
{
    "Response": {
        "Code": 1,
        "Msg": "abc",
        "AsyncRequestId": "abc",
        "RequestId": "abc"
    }
}
```

