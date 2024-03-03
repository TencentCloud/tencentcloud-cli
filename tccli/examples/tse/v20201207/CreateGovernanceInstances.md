**Example 1: 创建治理中心服务实例**



Input: 

```
tccli tse CreateGovernanceInstances --cli-unfold-argument  \
    --InstanceId xx \
    --GovernanceInstances.0.Protocol xx \
    --GovernanceInstances.0.Service xx \
    --GovernanceInstances.0.Weight 1 \
    --GovernanceInstances.0.Healthy True \
    --GovernanceInstances.0.Namespace xx \
    --GovernanceInstances.0.Isolate True \
    --GovernanceInstances.0.EnableHealthCheck True \
    --GovernanceInstances.0.Host xx \
    --GovernanceInstances.0.Ttl 1 \
    --GovernanceInstances.0.InstanceVersion xx \
    --GovernanceInstances.0.Port 1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

