**Example 1: 查询预测式外呼任务示例**

查询预测式外呼任务

Input: 

```
tccli ccc DescribePredictiveDialingCampaign --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --CampaignId 2569
```

Output: 
```
{
    "Response": {
        "CampaignId": 2569,
        "Name": "新能源SUV推荐",
        "CallOrder": 0,
        "SkillGroupId": 255,
        "IVRId": 4600,
        "Priority": 3,
        "ExpectedAbandonRate": 10,
        "RetryTimes": 1,
        "RetryInterval": 1800,
        "StartTime": 1708483433,
        "EndTime": 1708485433,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

