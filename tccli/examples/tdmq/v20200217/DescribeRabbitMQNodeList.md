**Example 1: RabbitMQ专享版查询节点列表**

RabbitMQ专享版查询节点列表 在查询节点的时候使用。

Input: 

```
tccli tdmq DescribeRabbitMQNodeList --cli-unfold-argument  \
    --InstanceId amqp-testtesttest \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "NodeList": [
            {
                "NodeName": "xx"
            }
        ]
    }
}
```

