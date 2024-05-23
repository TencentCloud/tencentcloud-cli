**Example 1: 创建成员企业激活记录**

通过此接口，创建子企业激活记录，集团企业管理员可针对未激活的成员企业进行授权。

Input: 

```
tccli ess CreateIntegrationSubOrganizationActiveRecord --cli-unfold-argument  \
    --Operator.UserId abc \
    --SubOrganizationIds 123456
```

Output: 
```
{
    "Response": {
        "FailedSubOrganizationIds": [],
        "RequestId": "yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF"
    }
}
```

