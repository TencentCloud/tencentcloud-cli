**Example 1: 查询RabbitMQ 用户列表**

-

Input: 

```
tccli tdmq DescribeRabbitMQUser --cli-unfold-argument  \
    --InstanceId amqp-44w9928j
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs",
        "RabbitMQUserList": [
            {
                "InstanceId": "amqp-xxx",
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

