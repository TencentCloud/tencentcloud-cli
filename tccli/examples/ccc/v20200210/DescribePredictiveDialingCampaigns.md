**Example 1: 查询预测式外呼任务列表示例**

查询预测式外呼任务列表

Input: 

```
tccli ccc DescribePredictiveDialingCampaigns --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --PageSize 25 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 66,
        "CampaignList": [
            {
                "CampaignId": 2567,
                "Name": "新能源SUV推荐1",
                "Status": 0,
                "StatusReason": 0,
                "CalleeCount": 1000,
                "FinishedCalleeCount": 0,
                "Priority": 3,
                "SkillGroupId": 255
            },
            {
                "CampaignId": 2568,
                "Name": "新能源SUV推荐2",
                "Status": 0,
                "StatusReason": 0,
                "CalleeCount": 1000,
                "FinishedCalleeCount": 0,
                "Priority": 3,
                "SkillGroupId": 255
            },
            {
                "CampaignId": 2569,
                "Name": "新能源SUV推荐3",
                "Status": 0,
                "StatusReason": 0,
                "CalleeCount": 1000,
                "FinishedCalleeCount": 0,
                "Priority": 3,
                "SkillGroupId": 255
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

