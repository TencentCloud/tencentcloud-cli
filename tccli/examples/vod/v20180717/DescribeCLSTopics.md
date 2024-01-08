**Example 1: 查询指定日志主题**



Input: 

```
tccli vod DescribeCLSTopics --cli-unfold-argument  \
    --CLSRegion ap-guangzhou \
    --LogsetId 54079098-61ea-48f9-8270-3b041a5d0150 \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Topics": [
            {
                "TopicId": "780ba384-5bc1-4cb1-a0e9-0cf8fafd3ee0",
                "TopicName": "mytopic",
                "LogsetId": "54079098-61ea-48f9-8270-3b041a5d0150"
            }
        ],
        "RequestId": "xxx"
    }
}
```

