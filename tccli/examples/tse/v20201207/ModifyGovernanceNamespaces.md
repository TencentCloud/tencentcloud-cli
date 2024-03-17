**Example 1: 修改治理中心命名空间**



Input: 

```
tccli tse ModifyGovernanceNamespaces --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceNamespaces.0.Name abc \
    --GovernanceNamespaces.0.Comment abc \
    --GovernanceNamespaces.0.UserIds abc \
    --GovernanceNamespaces.0.GroupIds abc \
    --GovernanceNamespaces.0.RemoveUserIds abc \
    --GovernanceNamespaces.0.RemoveGroupIds abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

