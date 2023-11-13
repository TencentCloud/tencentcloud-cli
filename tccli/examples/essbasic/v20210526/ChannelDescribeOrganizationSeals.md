**Example 1: 查询子客企业电子印章**

1.查询应用yDwhxUUckp3gl8j5UuFX33LSNozpRsbi下认证的子客org_dianziqian的印章
2.设置InfoType=1，返回时会同时返回授权用例的相关信息

Input: 

```
tccli essbasic ChannelDescribeOrganizationSeals --cli-unfold-argument  \
    --InfoType 1 \
    --Limit 1 \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8ff****2-be87-af68a7842493",
        "Seals": [
            {
                "AuthorizedUsers": [
                    {
                        "OpenId": "xxxtest1"
                    }
                ],
                "CreateOn": 163549000069,
                "Creator": "xxxtest1",
                "FailReason": "",
                "IsAllTime": true,
                "SealId": "yDxHTUUgydj94zlcUuO4zjESIzF*****",
                "SealName": "测试环境_测试",
                "SealPolicyId": "",
                "SealStatus": "SUCCESS",
                "SealType": "OFFICIAL",
                "Url": "https://***************.jpg"
            }
        ],
        "TotalCount": 35
    }
}
```

