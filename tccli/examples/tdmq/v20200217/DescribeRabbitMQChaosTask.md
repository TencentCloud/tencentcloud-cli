**Example 1: 获取 RabbitMQ 混沌测试任务的状态**



Input: 

```
tccli tdmq DescribeRabbitMQChaosTask --cli-unfold-argument  \
    --TaskId e43797fb-1837-4ea2-b0cd-1105468bd122
```

Output: 
```
{
    "Response": {
        "Status": "succeed",
        "Msg": "succeed",
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

