**Example 1: 实际受影响资产**

实际受影响资产

Input: 

```
tccli ctem DescribePocAssetData --cli-unfold-argument  \
    --VulId SC-2023-0677
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Banner": "",
                "CustomerId": 100150,
                "CustomerName": "腾讯公司",
                "IsAffected": true,
                "ScreenshotUrl": "",
                "Title": "测试网站",
                "Url": "1.1.1.1:2095"
            }
        ],
        "Total": 10,
        "RequestId": "eae76a33-a923-4ed0-a6b8-9641a744d365"
    }
}
```

