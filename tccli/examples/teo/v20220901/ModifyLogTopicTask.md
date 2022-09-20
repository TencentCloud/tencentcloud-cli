**Example 1: 修改推送任务**



Input: 

```
tccli teo ModifyLogTopicTask --cli-unfold-argument  \
    --TopicId 0a396698-d589-42b6-a6a2-701777d3afe0 \
    --LogSetId 33a900b2-9860-4da0-be91-bcce94c290ce \
    --EntityType application \
    --Period 11 \
    --ZoneId zone-28569s6od5na \
    --LogSetRegion ap-guangzhou \
    --LogSetName new_log_set \
    --TopicName new_topic_name
```

Output: 
```
{
    "Response": {
        "RequestId": "952c708d-abaf-464c-84cf-d1447887cf65"
    }
}
```

