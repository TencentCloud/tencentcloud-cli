**Example 1:  IP风险查询接口**



Input: 

```
tccli rce ManageIPPortraitRisk --cli-unfold-argument  \
    --PostTime 1766633688 \
    --BusinessSecurityData.UserIp 123.***.**.2 \
    --BusinessSecurityData.Channel 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "RiskScore": 0,
                "RiskType": [],
                "UserIp": "123.***.**.2"
            }
        },
        "RequestId": "42cd52a1-****-****-81c1-f40266b1dde6"
    }
}
```

