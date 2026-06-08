**Example 1: DescribeTokenPlanApiKeyUsageDetail**



Input: 

```
tccli tokenhub DescribeTokenPlanApiKeyUsageDetail --cli-unfold-argument  \
    --TeamId team-123456
```

Output: 
```
{
    "Response": {
        "Context": "",
        "List": [
            {
                "CacheToken": 0,
                "OutputToken": 39,
                "ApiKeyId": "ak-tp-20260408-123456",
                "RequestTime": "2026-04-10T14:24:45Z",
                "ModelName": "auto",
                "Uin": "123456",
                "RequestId": "451d5d39-9ed9-46f8-8dce-df582c3b2d0e",
                "InputToken": 66,
                "TotalToken": 105
            }
        ],
        "ListOver": true,
        "RequestId": "409be278-ce7c-4362-93a5-62391cdf4256"
    }
}
```

