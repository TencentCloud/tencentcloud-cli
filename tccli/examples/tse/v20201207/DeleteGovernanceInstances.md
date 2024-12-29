**Example 1: 删除服务实例**



Input: 

```
tccli tse DeleteGovernanceInstances --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceInstances.0.Service service \
    --GovernanceInstances.0.Namespace namespace \
    --GovernanceInstances.0.Host 127.0.0.1 \
    --GovernanceInstances.0.Port 1 \
    --GovernanceInstances.0.Id id
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

