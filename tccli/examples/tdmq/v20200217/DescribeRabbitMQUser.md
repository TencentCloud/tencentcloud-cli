**Example 1: 查询RabbitMQ 用户列表**

-

Input: 

```
tccli tdmq DescribeRabbitMQUser --cli-unfold-argument  \
    --InstanceId amqp-test
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "RabbitMQUserList": [
            {
                "ModifyTime": "1",
                "CreateTime": "1",
                "MaxChannels": 1,
                "MaxConnections": 1,
                "Type": "1",
                "InstanceId": "amqp-test",
                "User": "testVhost",
                "Password": "123",
                "Description": "hello",
                "Tags": [
                    "shop"
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

