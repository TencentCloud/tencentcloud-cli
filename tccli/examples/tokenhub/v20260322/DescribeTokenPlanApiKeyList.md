**Example 1: DescribeTokenPlanApiKeyList**



Input: 

```
tccli tokenhub DescribeTokenPlanApiKeyList --cli-unfold-argument  \
    --TeamId team-3a834f2dbcf48840115cbf4b48f25342 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ApiKeySet": [
            {
                "AllowedModels": "[\"glm-5\"]",
                "ApiKey": "sk-tp-****lQw0",
                "ApiKeyId": "ak-tp-20260407-cd2b616ac0ce4d89ffc0f8be03220606",
                "AppId": "1300056794",
                "CreatedAt": "2026-05-25T15:04:10+08:00",
                "Creator": "600000563014",
                "KeyVersion": 1,
                "Name": "syytest1111",
                "Status": "enable",
                "StopReason": "",
                "TeamId": "team-3a834f2dbcf48840115cbf4b48f25342",
                "Uin": "600000563014",
                "UpdatedAt": "2026-05-25T15:04:26+08:00",
                "UseStatus": "enable"
            }
        ],
        "RequestId": "c2e09e22-f9eb-4881-b1a2-7f9f170381d3",
        "TotalCount": 47
    }
}
```

