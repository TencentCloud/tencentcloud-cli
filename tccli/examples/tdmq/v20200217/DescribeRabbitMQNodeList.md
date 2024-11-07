**Example 1: RabbitMQ专享版查询节点列表**

RabbitMQ专享版查询节点列表 在查询节点的时候使用。

Input: 

```
tccli tdmq DescribeRabbitMQNodeList --cli-unfold-argument  \
    --InstanceId amqp-test \
    --Offset 0 \
    --Limit 3 \
    --NodeName rabbit@rabbitmq-broker-1.rabbitmq-broker-internal.amqp-test.svc.cluster.local \
    --Filters.0.Name nodeStatus \
    --Filters.0.Values running \
    --SortElement cpuUsage \
    --SortOrder descend
```

Output: 
```
{
    "Response": {
        "NodeList": [
            {
                "CPUUsage": "0.000%",
                "DiskUsage": "3.000%",
                "Memory": 171,
                "NodeName": "rabbit@rabbitmq-broker-1.rabbitmq-broker-internal.amqp-test.svc.cluster.local",
                "NodeStatus": "running",
                "ProcessNumber": 459
            }
        ],
        "RequestId": "a95bfcfd-8388-4f86-8511-ca3be8ed000c",
        "TotalCount": 1
    }
}
```

