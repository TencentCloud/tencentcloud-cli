**Example 1:  IP风险查询接口**



Input: 

```
tccli rce ManageIPPortraitRisk --cli-unfold-argument  \
    --PostTime 1686263179 \
    --BusinessSecurityData.UserIp 203.***.***.118 \
    --BusinessSecurityData.Channel 6
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK"
        },
        "RequestId": "be7d30aa-a824-4b5d-9b53-288e9dae2423"
    }
}
```

