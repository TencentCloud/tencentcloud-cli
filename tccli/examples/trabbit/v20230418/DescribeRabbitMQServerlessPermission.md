**Example 1: 查询RabbitMQ权限列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessPermission --cli-unfold-argument  \
    --InstanceId amqp-slfxemauoa \
    --Offset 0 \
    --Limit 20 \
    --VirtualHost  \
    --User 
```

Output: 
```
{
    "Response": {
        "RequestId": "8edba56c-fe02-4e15-8e56-af2a7c4d3760",
        "TotalCount": 1,
        "RabbitMQPermissionList": [
            {
                "InstanceId": "amqp-slfxemauoa",
                "User": "test_role",
                "VirtualHost": "test_vhost3213",
                "ConfigRegexp": ".*",
                "WriteRegexp": ".*",
                "ReadRegexp": ".*",
                "CreateTime": "2025-01-16 19:52:53",
                "ModifyTime": "2025-01-16 19:52:53"
            }
        ]
    }
}
```

