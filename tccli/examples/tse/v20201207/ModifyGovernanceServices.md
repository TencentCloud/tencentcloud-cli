**Example 1: 修改治理中心服务**



Input: 

```
tccli tse ModifyGovernanceServices --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceServices.0.Name serviceName \
    --GovernanceServices.0.Namespace serviceNamespace \
    --GovernanceServices.0.Comment serviceCommtent \
    --GovernanceServices.0.Metadatas.0.Key keyName \
    --GovernanceServices.0.Metadatas.0.Value ValueName \
    --GovernanceServices.0.Department DepartmentName \
    --GovernanceServices.0.Business BusinessName \
    --GovernanceServices.0.UserIds user-id \
    --GovernanceServices.0.GroupIds group-id \
    --GovernanceServices.0.RemoveUserIds user-id \
    --GovernanceServices.0.RemoveGroupIds group-id
```

Output: 
```
{
    "Response": {
        "RequestId": "request-id"
    }
}
```

