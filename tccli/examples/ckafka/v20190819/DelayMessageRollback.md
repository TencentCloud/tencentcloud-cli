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
        "RequestId": "dda6e5eb-eefa-41c9-9ee5-d92942a2987a"
    }
}
```

