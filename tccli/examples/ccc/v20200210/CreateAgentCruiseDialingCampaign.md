**Example 1: 创建座席巡航式外呼任务实例**

创建座席巡航式外呼任务

Input: 

```
tccli ccc CreateAgentCruiseDialingCampaign --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --Name 新能源SUV推荐 \
    --Callees +8613012345678 +8613012345679 +8613012345670 \
    --Callers 0086075586013388 \
    --Agent foo@tencent.com \
    --ConcurrencyNumber 3 \
    --CallOrder 0 \
    --StartTime 1708483433 \
    --EndTime 1708485433
```

Output: 
```
{
    "Response": {
        "CampaignId": 2569,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

