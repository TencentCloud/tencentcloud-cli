**Example 1: 修改跨账号投递任务**



Input: 

```
tccli cls ModifyCLSDeliverTask --cli-unfold-argument  \
    --TaskId 3f2cdda9-263e-47fe-8bde-bb3c541e45e6 \
    --TargetTopicConfig.AccountType 1 \
    --TargetTopicConfig.Region ap-******* \
    --TargetTopicConfig.LogsetId 16bcb721-0101-4c6f-8c4c-aa0e290ab5da \
    --TargetTopicConfig.TopicId 32d29136-bdfc-4749-928b-a0b24d62a3b8 \
    --HasServicesLog 1 \
    --TaskName b*******_update
```

Output: 
```
{
    "Response": {
        "RequestId": "7f4416ef-3255-4b9b-8207-1738b290fbac"
    }
}
```

