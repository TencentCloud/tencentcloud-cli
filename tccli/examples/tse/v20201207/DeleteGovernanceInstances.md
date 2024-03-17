**Example 1: 删除服务实例**



Input: 

```
tccli tse DeleteGovernanceInstances --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceInstances.0.Service abc \
    --GovernanceInstances.0.Namespace abc \
    --GovernanceInstances.0.Host abc \
    --GovernanceInstances.0.Port 1 \
    --GovernanceInstances.0.Id abc
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

