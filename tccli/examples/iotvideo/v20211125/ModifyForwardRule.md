**Example 1: 修改转发规则**



Input: 

```
tccli iotvideo ModifyForwardRule --cli-unfold-argument  \
    --Skey xrnWgKu0fCz7q8JIQYFiNP-XpyaziljFvrQg4A*Cidc_ \
    --ProductID PV1674YINM \
    --MsgType 3 \
    --QueueRegion ap-guangzhou \
    --QueueType 1 \
    --QueueName iot_hub_test \
    --InstanceId ckafka-cy614eit \
    --InstanceName iot_test_no_delete
```

Output: 
```
{
    "Response": {
        "Endpoint": "100004557990",
        "RequestId": "4eeccf4d-65e9-495f-8ac8-d4b84d373c1d",
        "ProductID": "PV1674YINM",
        "Result": 0,
        "ErrMsg": "",
        "QueueType": 1
    }
}
```

