**Example 1: 查询 座席巡航式外呼任务示例**



Input: 

```
tccli ccc DescribeAgentCruiseDialingCampaign --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --CampaignId 2569
```

Output: 
```
{
    "Response": {
        "Name": "新能源SUV推荐",
        "Agent": "foo@tencent.com",
        "ConcurrencyNumber": 3,
        "CallOrder": 0,
        "StartTime": 1708483433,
        "EndTime": 1708485433,
        "UUI": "",
        "State": 2,
        "TotalCalleeCount": 200,
        "CalledCalleeCount": 200,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

