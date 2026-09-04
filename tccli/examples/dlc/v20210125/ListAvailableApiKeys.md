**Example 1: 测试**



Input: 

```
tccli dlc ListAvailableApiKeys --cli-unfold-argument  \
    --Page 1 \
    --PageSize 50
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ApiKey": "sk-proj-iXCM3DWle49o6vYuL4zKvk2mI8mpTCBcd05aMmIiJR6Cp5Kf",
                "ApiKeyId": "apikey-20260615162055-v6s0",
                "AppId": 260200066,
                "CreateTime": 1781511655412,
                "Name": "qzzhu_061501-key-20260615162055-zm6f",
                "Status": "Revoked",
                "SubAccountUin": "700002655694",
                "Uin": "700002655694",
                "UpdateTime": 1781511966690
            }
        ],
        "Page": 1,
        "PageSize": 50,
        "Total": 49,
        "TotalPages": 1,
        "RequestId": "6b98ff6c-6918-4bf6-8d58-c555094f348d"
    }
}
```

