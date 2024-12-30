**Example 1: 修改治理中心服务实例**



Input: 

```
tccli tse ModifyGovernanceInstances --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceInstances.0.Service service-name \
    --GovernanceInstances.0.Namespace namespace \
    --GovernanceInstances.0.Weight 1 \
    --GovernanceInstances.0.Healthy True \
    --GovernanceInstances.0.Isolate True \
    --GovernanceInstances.0.Host 127.0.0.1 \
    --GovernanceInstances.0.Port 1 \
    --GovernanceInstances.0.Protocol tcp \
    --GovernanceInstances.0.InstanceVersion prod \
    --GovernanceInstances.0.EnableHealthCheck True \
    --GovernanceInstances.0.Ttl 1 \
    --GovernanceInstances.0.Id id \
    --GovernanceInstances.0.Metadatas.0.Key key \
    --GovernanceInstances.0.Metadatas.0.Value key
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

