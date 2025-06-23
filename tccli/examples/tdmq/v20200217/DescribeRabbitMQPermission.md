**Example 1: 查询RabbitMQ权限列表**



Input: 

```
tccli tdmq DescribeRabbitMQPermission --cli-unfold-argument  \
    --InstanceId amqp-2ppxx4rq
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RabbitMQPermissionList": [
            {
                "InstanceId": "amqp-2ppxx4rq",
                "User": "admin",
                "VirtualHost": "testVhost",
                "ConfigRegexp": ".*",
                "WriteRegexp": ".*",
                "ReadRegexp": ".*",
                "CreateTime": "2022-12-16 11:19:56",
                "ModifyTime": "2022-12-16 11:29:56"
            }
        ],
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

