**Example 1: 创建普通主题**



Input: 

```
tccli trocket CreateTopic --cli-unfold-argument  \
    --InstanceId rmq-16jm9787qv \
    --Topic test_normal_topic \
    --TopicType NORMAL \
    --QueueNum 3 \
    --Remark test remark \
    --MsgTTL 72
```

Output: 
```
{
    "Response": {
        "InstanceId": "rmq-16jm9787qv",
        "Topic": "test_normal_topic",
        "RequestId": "08087f18-5882-4d01-81c2-696b69404926"
    }
}
```

**Example 2: 创建轻量主题**



Input: 

```
tccli trocket CreateTopic --cli-unfold-argument  \
    --InstanceId rmq-16jm9787qv \
    --Topic test_lite_topic \
    --TopicType LITE \
    --QueueNum 3 \
    --Remark test remark \
    --MsgTTL 72 \
    --AutoExpireDelete True \
    --AutoExpireTime 1800
```

Output: 
```
{
    "Response": {
        "InstanceId": "rmq-16jm9787qv",
        "Topic": "test_lite_topic",
        "RequestId": "201510ab-d42c-4bc6-81d2-50ba9a10d60c"
    }
}
```

