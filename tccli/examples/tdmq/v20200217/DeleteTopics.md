**Example 1: 删除主题列表**



Input: 

```
tccli tdmq DeleteTopics --cli-unfold-argument  \
    --TopicSets.0.EnvironmentId abc \
    --TopicSets.0.TopicName abc \
    --ClusterId abc \
    --EnvironmentId abc \
    --Force True
```

Output: 
```
{
    "Response": {
        "TopicSets": [
            {
                "EnvironmentId": "default",
                "TopicName": "cloud_test_1"
            }
        ],
        "RequestId": "5f4eabe4-94f2-4f91-8285-86f24ef8bcfa"
    }
}
```

