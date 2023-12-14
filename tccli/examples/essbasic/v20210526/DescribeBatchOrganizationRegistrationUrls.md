**Example 1: 查询批量企业认证**



Input: 

```
tccli essbasic DescribeBatchOrganizationRegistrationUrls --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId ceshi \
    --Agent.ProxyOrganizationOpenId ceshi_org \
    --Agent.AppId 60e16350b0361c888ecb30477d2c16e9 \
    --TaskId yDSxSUUxxxxxxxx21JXBlJZsaj
```

Output: 
```
{
    "Response": {
        "OrganizationAuthUrls": [
            {
                "AuthUrl": "https://test.qian.tencent.cn/console/batch-register?token=yDxxxxxxxxxgENliu9LD&orgName=典子谦批量认证企业",
                "ErrorMessage": ""
            }
        ],
        "RequestId": "s1702447767875624775"
    }
}
```

