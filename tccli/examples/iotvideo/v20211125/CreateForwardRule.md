**Example 1: 创建转发规则**

创建转发规则

Input: 

```
tccli iotvideo CreateForwardRule --cli-unfold-argument  \
    --Skey xrnWgKu0fCz7q8JIQYFiNP-XpyaziljFvrQg4A*Cidc_ \
    --ProductID TIUHIHHII \
    --MsgType 3 \
    --QueueRegion ap-guangzhou \
    --QueueType 1 \
    --QueueName hub_test_topic \
    --InstanceId ckafka-cy614eit \
    --InstanceName iot_test_no_delete
```

Output: 
```
{
    "Response": {
        "ProductID": "TDCZ2WD29Z",
        "InstanceId": "",
        "InstanceName": "",
        "Endpoint": "100004557990",
        "Result": 0,
        "QueueRegion": "ap-guangzhou",
        "QueueName": "hub_test_topic",
        "RoleName": "cmqIOTRole100004557990_1522374592",
        "MsgType": 3,
        "RoleID": 16576,
        "ErrMsg": "",
        "QueueType": 1,
        "RequestId": "d5c0b643-8a2d-4f03-8207-40c4602c652d"
    }
}
```

