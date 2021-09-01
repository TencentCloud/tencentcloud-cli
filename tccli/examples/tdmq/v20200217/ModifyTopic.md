**Example 1: 修改主题属性**



Input: 

```
tccli tdmq ModifyTopic --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName test_topic \
    --Partitions 3 \
    --Remark 修改分区为3
```

Output: 
```
{
    "Response": {
        "Partitions": 3,
        "Remark": "修改分区为3",
        "RequestId": "c276a96f-1612-47ad-9562-da06d4fdf1ed"
    }
}
```

