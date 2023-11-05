**Example 1: 员工离职**

员工离职只需要指定他们的ID(即OpenId)即可

Input: 

```
tccli essbasic SyncProxyOrganizationOperators --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperatorType RESIGN \
    --ProxyOrganizationOperators.0.Id n123456 \
    --ProxyOrganizationOperators.1.Id n13579
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "FailedList": [],
        "RequestId": "1c92341e-184c-4322-8fe2-187411865280"
    }
}
```

**Example 2: 新增员工**

新增2个员工成功

Input: 

```
tccli essbasic SyncProxyOrganizationOperators --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperatorType CREATE \
    --ProxyOrganizationOperators.0.Id n02468 \
    --ProxyOrganizationOperators.0.Name 张三 \
    --ProxyOrganizationOperators.0.IdCardNumber 640425****01015373 \
    --ProxyOrganizationOperators.0.Mobile 18888888888 \
    --ProxyOrganizationOperators.1.Id n123456 \
    --ProxyOrganizationOperators.1.Name 李四 \
    --ProxyOrganizationOperators.1.IdCardNumber 610124****01016474 \
    --ProxyOrganizationOperators.1.Mobile 15100000000
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "FailedList": [],
        "RequestId": "88a7d888-f805-4bdc-a690-1a9d65d1e159"
    }
}
```

