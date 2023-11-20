**Example 1: 导入源集群主题列表**



Input: 

```
tccli trocket ImportSourceClusterTopics --cli-unfold-argument  \
    --TaskId abc \
    --TopicList.0.TopicName Test \
    --TopicList.0.TopicType Normal \
    --TopicList.0.QueueNum 10 \
    --TopicList.0.Remark abc \
    --TopicList.0.Namespace 
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

