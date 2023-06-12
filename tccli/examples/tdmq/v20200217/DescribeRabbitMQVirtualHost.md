**Example 1: 查询RabbitMQ vhost列表**

-

Input: 

```
tccli tdmq DescribeRabbitMQVirtualHost --cli-unfold-argument  \
    --InstanceId amqp-44w9928j
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs",
        "VirtualHostList": [
            {
                "InstanceId": "amqp-xxx",
                "VirtualHost": "testVhost",
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

