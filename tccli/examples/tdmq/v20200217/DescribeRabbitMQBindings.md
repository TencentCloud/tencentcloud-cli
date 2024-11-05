**Example 1: 查询RabbitMQ路由关系列表**



Input: 

```
tccli tdmq DescribeRabbitMQBindings --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost test
```

Output: 
```
{
    "Response": {
        "BindingInfoList": [
            {
                "BindingId": 0,
                "VirtualHost": "abc",
                "Source": "abc",
                "DestinationType": "abc",
                "Destination": "abc",
                "RoutingKey": "abc",
                "SourceExchangeType": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

