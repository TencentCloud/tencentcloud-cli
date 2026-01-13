**Example 1: 修改 RabbitMQ 专享版实例**



Input: 

```
tccli tdmq ModifyRabbitMQVipInstance --cli-unfold-argument  \
    --InstanceId amqp-44ordrrj \
    --ClusterName 生产实例名称
```

Output: 
```
{
    "Response": {
        "InstanceId": "amqp-44ordrrj",
        "RequestId": "47638f78-d85a-46aa-a43d-59db21bc7c72"
    }
}
```

