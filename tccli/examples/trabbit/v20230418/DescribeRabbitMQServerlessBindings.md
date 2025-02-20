**Example 1: 查询路由绑定信息**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessBindings --cli-unfold-argument  \
    --InstanceId amqp-slfxemauoa \
    --VirtualHost test_vhost3213 \
    --Offset 0 \
    --Limit 20 \
    --SourceExchange test_exchange
```

Output: 
```
{
    "Response": {
        "RequestId": "99ff7b6b-bc6e-48e7-8ef6-cffcf74393f6",
        "TotalCount": 1,
        "BindingInfoList": [
            {
                "BindingId": 18921,
                "VirtualHost": "test_vhost3213",
                "Source": "test_exchange",
                "DestinationType": "queue",
                "Destination": "test_queue",
                "RoutingKey": "testRoutingKey",
                "SourceExchangeType": "direct",
                "CreateTime": "2025-01-16 19:52:51",
                "ModifyTime": "2025-01-16 19:52:51"
            }
        ]
    }
}
```

