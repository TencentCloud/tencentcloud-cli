**Example 1: 创建服务实例**



Input: 

```
tccli tse CreateGovernanceInstances --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceInstances.0.Service service \
    --GovernanceInstances.0.Namespace namespace \
    --GovernanceInstances.0.Weight 1 \
    --GovernanceInstances.0.Healthy True \
    --GovernanceInstances.0.Isolate True \
    --GovernanceInstances.0.Host 127.0.0.1 \
    --GovernanceInstances.0.Port 1 \
    --GovernanceInstances.0.Protocol tcp \
    --GovernanceInstances.0.InstanceVersion prod \
    --GovernanceInstances.0.EnableHealthCheck True \
    --GovernanceInstances.0.Ttl 1
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

