**Example 1: 创建治理中心命名空间**

创建治理中心命名空间

Input: 

```
tccli tse CreateGovernanceNamespaces --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceNamespaces.0.Name name \
    --GovernanceNamespaces.0.Comment comment \
    --GovernanceNamespaces.0.UserIds 101 \
    --GovernanceNamespaces.0.GroupIds groupa \
    --GovernanceNamespaces.0.RemoveUserIds 101 \
    --GovernanceNamespaces.0.RemoveGroupIds groupa \
    --GovernanceNamespaces.0.ServiceExportTo json
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "req-id"
    }
}
```

