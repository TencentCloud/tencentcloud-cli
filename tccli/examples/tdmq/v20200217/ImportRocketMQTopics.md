**Example 1: 导入主题列表**

导入主题列表

Input: 

```
tccli tdmq ImportRocketMQTopics --cli-unfold-argument  \
    --Topics.0.Namespace test_ns \
    --Topics.0.TopicName test_topic \
    --Topics.0.Type Normal \
    --Topics.0.Partitions 3 \
    --Topics.0.Remark remark info \
    --TaskId 700000780519-o4n3m5g97wgr-3391d15d
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "73996928-797f-445a-9572-25ed6c588d30"
    }
}
```

