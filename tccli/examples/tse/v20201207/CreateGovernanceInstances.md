**Example 1: 创建服务实例**



Input: 

```
tccli tse CreateGovernanceInstances --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceInstances.0.Service abc \
    --GovernanceInstances.0.Namespace abc \
    --GovernanceInstances.0.Weight 1 \
    --GovernanceInstances.0.Healthy True \
    --GovernanceInstances.0.Isolate True \
    --GovernanceInstances.0.Host abc \
    --GovernanceInstances.0.Port 1 \
    --GovernanceInstances.0.Protocol abc \
    --GovernanceInstances.0.InstanceVersion abc \
    --GovernanceInstances.0.EnableHealthCheck True \
    --GovernanceInstances.0.Ttl 1
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

