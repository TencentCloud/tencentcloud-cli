**Example 1: 查询RabbitMQ exchange 列表**

查询RabbitMQ exchange 列表

Input: 

```
tccli tdmq DescribeRabbitMQExchanges --cli-unfold-argument  \
    --InstanceId amqp-2ppxx4rq \
    --VirtualHost vhost1
```

Output: 
```
{
    "Response": {
        "RequestId": "request1",
        "ExchangeInfoList": [
            {
                "ExchangeName": "test1",
                "ExchangeType": "fanout",
                "Remark": "test1",
                "VirtualHost": "vhost1",
                "ExchangeCreator": "user",
                "CreateTimeStamp": "2022-12-04 01:08:43",
                "ModTimeStamp": "2022-12-04 01:08:43"
            },
            {
                "ExchangeName": "test2",
                "ExchangeType": "direct",
                "Remark": "test2",
                "VirtualHost": "vhost1",
                "ExchangeCreator": "user",
                "CreateTimeStamp": "2022-12-04 01:08:43",
                "ModTimeStamp": "2022-12-04 01:08:43"
            }
        ],
        "TotalCount": 2
    }
}
```

