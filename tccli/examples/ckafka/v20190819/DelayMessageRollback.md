**Example 1: 生产消费延迟恢复**

生产消费延迟恢复

Input: 

```
tccli ckafka DelayMessageRollback --cli-unfold-argument  \
    --InstanceId abc
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

