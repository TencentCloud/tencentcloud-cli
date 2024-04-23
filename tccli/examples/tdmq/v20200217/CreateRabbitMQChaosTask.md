**Example 1: 创建 RabbitMQ 混沌测试任务**



Input: 

```
tccli tdmq CreateRabbitMQChaosTask --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --ZoneId 800001 \
    --Type crash
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

