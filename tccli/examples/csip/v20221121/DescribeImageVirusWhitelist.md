**Example 1: 查询镜像木马白名单**



Input: 

```
tccli csip DescribeImageVirusWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "WhiteList": [
            {
                "ImageIds": 1,
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "7000********",
                "Remark": "木马白名单",
                "RuleId": 1,
                "Scope": 1
            }
        ],
        "RequestId": "5a1c2b01-7534-456c-8071-ec6bff2c2886"
    }
}
```

