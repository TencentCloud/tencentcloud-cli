**Example 1: 查询预测式外呼呼叫列表示例**

查询预测式外呼呼叫列表

Input: 

```
tccli ccc DescribePredictiveDialingSessions --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --CampaignId 2569 \
    --PageSize 25 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 66,
        "SessionList": [
            "a5be1044-e8b0-4f02-9b25-64baee24374b",
            "22c3e170-f307-47c8-9f10-1b77413a646f",
            "e8557b17-d68b-4475-9a97-639a1108887b"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

