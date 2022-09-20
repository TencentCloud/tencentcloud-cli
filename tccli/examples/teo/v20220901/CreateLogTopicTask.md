**Example 1: 创建推送任务**



Input: 

```
tccli teo CreateLogTopicTask --cli-unfold-argument  \
    --LogSetRegion ap-guangzhou \
    --ZoneName hello.club \
    --ZoneId zone-28569s6od5na \
    --EntityType application \
    --Period 10 \
    --TopicName test_topic \
    --TaskName test_task \
    --EntityList test \
    --LogSetId 33a900b2-9860-4da0-be91-bcce94c290ce
```

Output: 
```
{
    "Response": {
        "TopicId": "ace8680b-55b9-498b-a113-056ab68d1da1",
        "RequestId": "40be710a-9706-4b22-865e-c9739111ef1a"
    }
}
```

