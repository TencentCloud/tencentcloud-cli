**Example 1: 创建投递任务**



Input: 

```
tccli cls CreateCLSDeliverTask --cli-unfold-argument  \
    --TaskName b*******_test_ap-tokyo_cross \
    --SourceTopicConfig.TopicFilterType 1 \
    --SourceTopicConfig.LogsetId ca5938d1-e027-409c-a345-16ce7b5e8d98 \
    --SourceTopicConfig.Topics.0.TopicId b*******-test-ok-1254077820 \
    --TargetTopicConfig.AccountType 1 \
    --TargetTopicConfig.Region ap-***** \
    --TargetTopicConfig.LogsetId 16bcb721-0101-4c6f-8c4c-aa0e290ab5da \
    --TargetTopicConfig.TopicId 32d29136-bdfc-4749-928b-a0b24d62a3b8 \
    --DeliverRule.DataScope 3 \
    --Compliance 1 \
    --HasServicesLog 2
```

Output: 
```
{
    "Response": {
        "TaskId": "5c1f1002-ceb1-4b45-a2f9-bcfc1fbd23ed",
        "RequestId": "2ade24da-8ed5-4680-bf2e-c2b9e1be01f8"
    }
}
```

