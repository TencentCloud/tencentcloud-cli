**Example 1: 查询RabbitMQ权限列表**

-

Input: 

```
tccli tdmq DescribeRabbitMQPermission --cli-unfold-argument  \
    --InstanceId amqp-jero744g
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RabbitMQPermissionList": [
            {
                "InstanceId": "amqp-jero744g",
                "User": "admin",
                "VirtualHost": "tdmq_data",
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

