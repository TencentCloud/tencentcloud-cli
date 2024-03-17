**Example 1: 创建治理中心服务**



Input: 

```
tccli tse CreateGovernanceServices --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceServices.0.Name abc \
    --GovernanceServices.0.Namespace abc \
    --GovernanceServices.0.Comment abc \
    --GovernanceServices.0.Metadatas.0.Key abc \
    --GovernanceServices.0.Metadatas.0.Value abc \
    --GovernanceServices.0.Department abc \
    --GovernanceServices.0.Business abc \
    --GovernanceServices.0.UserIds abc \
    --GovernanceServices.0.GroupIds abc \
    --GovernanceServices.0.RemoveUserIds abc \
    --GovernanceServices.0.RemoveGroupIds abc
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

