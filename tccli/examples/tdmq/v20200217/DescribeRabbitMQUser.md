**Example 1: 查询RabbitMQ 用户列表**



Input: 

```
tccli tdmq DescribeRabbitMQUser --cli-unfold-argument  \
    --InstanceId amqp-2ppxx4rq
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "RabbitMQUserList": [
            {
                "ModifyTime": "2024-06-06 22:46:38.000",
                "CreateTime": "2024-06-06 22:46:38.000",
                "MaxChannels": 1024,
                "MaxConnections": 1000,
                "Type": "1",
                "InstanceId": "amqp-2ppxx4rq",
                "User": "test_user",
                "Password": "Tencent123",
                "Description": "user description",
                "Tags": [
                    "user-tag"
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

