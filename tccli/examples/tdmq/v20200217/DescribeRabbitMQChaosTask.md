**Example 1: 获取 RabbitMQ 混沌测试任务的状态**



Input: 

```
tccli tdmq DescribeRabbitMQChaosTask --cli-unfold-argument  \
    --TaskId xxx
```

Output: 
```
{
    "Response": {
        "Status": "abc",
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

