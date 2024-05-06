**Example 1: 查询批量企业认证**



Input: 

```
tccli ess DescribeBatchOrganizationRegistrationUrls --cli-unfold-argument  \
    --Operator.UserId yDSxSUUxxxxxxxx21JXBlJZsaj \
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

