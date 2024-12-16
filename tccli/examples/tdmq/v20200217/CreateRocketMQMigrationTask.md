**Example 1: 添加迁移任务**



Input: 

```
tccli tdmq CreateRocketMQMigrationTask --cli-unfold-argument  \
    --Namespace abcd \
    --Topics.0.Namespace abcd \
    --Topics.0.Remark test \
    --Topics.0.Type Normal \
    --Topics.0.TopicName 123456 \
    --Topics.0.Partitions 2 \
    --ClusterId rocketmq-9npap34p9pa4 \
    --Type 0 \
    --Groups.0.ConsumeBroadcastEnable true \
    --Groups.0.GroupName test1 \
    --Groups.0.Remark testg \
    --Groups.0.Namespace abcd \
    --Groups.0.ConsumeEnable true
```

Output: 
```
{
    "Response": {
        "RequestId": "0484ec00-1ae3-4dec-872d-279d3ab83346"
    }
}
```

