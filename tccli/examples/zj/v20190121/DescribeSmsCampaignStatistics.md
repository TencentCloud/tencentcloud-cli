**Example 1: DescribeSmsCampaignStatistics**



Input: 

```
tccli zj DescribeSmsCampaignStatistics --cli-unfold-argument  \
    --License xxx \
    --CampaignId 1256886
```

Output: 
```
{
    "Response": {
        "Data": {
            "CampaignId": 123456,
            "Statistics": [
                {
                    "CrowdId": 123,
                    "CrowdName": "xx",
                    "CrowdCount": 123,
                    "TemplateList": [
                        {
                            "TemplateId": "xxx",
                            "TemplateContent": "xxx",
                            "SendCount": 123,
                            "ClickCount": 123
                        }
                    ]
                }
            ]
        },
        "RequestId": "87242041-7de8-4562-96ac-2d853eca3e44"
    }
}
```

