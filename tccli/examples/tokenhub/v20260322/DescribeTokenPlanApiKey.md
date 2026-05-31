**Example 1: DescribeTokenPlanApiKey**



Input: 

```
tccli tokenhub DescribeTokenPlanApiKey --cli-unfold-argument  \
    --ApiKeyId ak-tp-20260412-72dddac0126f0eadf4670f6ce63b3db1
```

Output: 
```
{
    "Response": {
        "ApiKey": {
            "AllowedModels": "[\"glm-5\", \"auto\"]",
            "ApiKey": "sk-tp-****L8py",
            "ApiKeyId": "ak-tp-20260412-72dddac0126f0eadf4670f6ce63b3db1",
            "AppId": "1300056794",
            "CreatedAt": "2026-04-12T20:10:47+08:00",
            "Creator": "600000563014",
            "KeyVersion": 1,
            "Name": "my-test-apikey",
            "Status": "enable",
            "StopReason": "NORMAL",
            "TPM": 0,
            "TeamId": "team-3a834f2dbcf48840115cbf4b48f25342",
            "Uin": "600000563014",
            "UpdatedAt": "2026-04-12T20:10:47+08:00",
            "UseStatus": "enable"
        },
        "RequestId": "b51cda8e-5153-4855-bc34-a2910ec682f9"
    }
}
```

