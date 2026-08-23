**Example 1: 查询容器镜像敏感信息白名单**



Input: 

```
tccli csip DescribeImageSensitiveWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WhiteList": [
            {
                "Behavior": 1,
                "ImageIds": [
                    1
                ],
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "Remark": "敏感信息白名单",
                "RuleId": 1,
                "Scope": 0,
                "Status": 0
            }
        ],
        "RequestId": "b0f177f7-540f-4118-af3e-e84d57636afa"
    }
}
```

