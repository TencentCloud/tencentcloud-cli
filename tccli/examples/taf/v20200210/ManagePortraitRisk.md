**Example 1: IP风险查询接口**



Input: 

```
tccli taf ManagePortraitRisk --cli-unfold-argument  \
    --BusinessSecurityData.PostTime 1686263179 \
    --BusinessSecurityData.UserIp 203.205.141.118
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "Level": 4,
                "UserIp": "203.205.141.118"
            }
        },
        "RequestId": "be7d30aa-a824-4b5d-9b53-288e9dae2423"
    }
}
```

