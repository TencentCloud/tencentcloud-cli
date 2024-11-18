**Example 1: 创建 RabbitMQ 混沌测试任务**



Input: 

```
tccli tdmq CreateRabbitMQChaosTask --cli-unfold-argument  \
    --InstanceId amqp-jero744g \
    --ZoneId 800001 \
    --Type crash
```

Output: 
```
{
    "Response": {
        "TaskId": "e43797fb-1837-4ea2-b0cd-1105468bd122",
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

