**Example 1: 修改治理中心命名空间**



Input: 

```
tccli tse ModifyGovernanceNamespaces --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceNamespaces.0.Name name \
    --GovernanceNamespaces.0.Comment coment \
    --GovernanceNamespaces.0.UserIds 101 \
    --GovernanceNamespaces.0.GroupIds groupa \
    --GovernanceNamespaces.0.RemoveUserIds 101 \
    --GovernanceNamespaces.0.RemoveGroupIds groupa
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

