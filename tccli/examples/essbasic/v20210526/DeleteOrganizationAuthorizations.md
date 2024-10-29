**Example 1: 批量清理张三的所有认证中的认证流**

1. 企业典子谦示例企业 通过生成批量认证接口生成了 两个认证企业 （张三示例企业一， 张三示例企业二）
2. 此时操作人典子谦示例企业 的业务员典子谦 发现超管应该是李四，信息填写错误，希望批量清除之前写错的信息，进行重新认证。
3. 此时传递超管的姓名和手机号， 来进行清理。
4. 全部清理成功，status 返回为 1

Input: 

```
tccli essbasic DeleteOrganizationAuthorizations --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --AdminName 张三 \
    --AdminMobile 18888888888
```

Output: 
```
{
    "Response": {
        "DeleteOrganizationAuthorizationInfos": [
            {
                "AuthorizationId": "yDCkRUUckp4mdtwzUuvjSCCEzIZPsM4A",
                "OrganizationName": "张三示例企业一",
                "OrganizationOpenId": "org_zhangsan_1"
            },
            {
                "AuthorizationId": "yDCkRUUckp4mdw8eUuYnzJiiRO2w2jQI",
                "OrganizationName": "张三示例企业一",
                "OrganizationOpenId": "org_zhangsan_2"
            }
        ],
        "RequestId": "37e81c99bc4e",
        "Status": 1
    }
}
```

