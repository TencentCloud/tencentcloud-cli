**Example 1: 创建治理中心服务**



Input: 

```
tccli tse CreateGovernanceServices --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceServices.0.Name name \
    --GovernanceServices.0.Namespace namespace \
    --GovernanceServices.0.Comment comment \
    --GovernanceServices.0.Metadatas.0.Key key \
    --GovernanceServices.0.Metadatas.0.Value value \
    --GovernanceServices.0.Department dev \
    --GovernanceServices.0.Business web \
    --GovernanceServices.0.UserIds 101 \
    --GovernanceServices.0.GroupIds groupa \
    --GovernanceServices.0.RemoveUserIds 101 \
    --GovernanceServices.0.RemoveGroupIds groupa
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

