**Example 1: 导入源集群主题列表**



Input: 

```
tccli trocket ImportSourceClusterTopics --cli-unfold-argument  \
    --TaskId 215d3ec6-70c9 \
    --TopicList.0.TopicName test_topic \
    --TopicList.0.TopicType Normal \
    --TopicList.0.QueueNum 3 \
    --TopicList.0.Remark 测试导入 \
    --TopicList.0.Namespace test_namespace
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "c5d126b6-aeeb-40ad-81c0-a94abd43f157"
    }
}
```

