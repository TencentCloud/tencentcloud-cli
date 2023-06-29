**Example 1: 获取产品转发规则**

获取产品转发规则

Input: 

```
tccli iotvideo DescribeForwardRule --cli-unfold-argument  \
    --Skey 1213123 \
    --QueueType 1 \
    --Consecretid fawefwe \
    --ProductID PTROMP3AOB
```

Output: 
```
{
    "Response": {
        "Endpoint": "1234141234",
        "QueueType": 1,
        "InstanceId": "topic-123aw",
        "RoleID": 123,
        "Result": 1,
        "MsgType": 1,
        "RequestId": "2172b7d1-9a49-4142-938a-ff4fa3d55881",
        "QueueRegion": "gz",
        "RoleName": "role-fawe",
        "InstanceName": "kafka-test",
        "QueueName": "kafka-t1132",
        "ErrMsg": "",
        "ProductID": "PTROMP3AOB"
    }
}
```

