**Example 1: 添加迁移任务**



Input: 

```
tccli tdmq CreateRocketMQMigrationTask --cli-unfold-argument  \
    --Namespace test_ns \
    --Topics.0.Namespace test_ns \
    --Topics.0.Remark test topic info. \
    --Topics.0.Type Normal \
    --Topics.0.TopicName test_topic \
    --Topics.0.Partitions 2 \
    --ClusterId rocketmq-9npap34p9pa4 \
    --Type 0 \
    --Groups.0.ConsumeBroadcastEnable true \
    --Groups.0.GroupName test_group \
    --Groups.0.Remark test group info. \
    --Groups.0.Namespace test_ns \
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

