**Example 1: 编辑域名**



Input: 

```
tccli waf ModifyHost --cli-unfold-argument  \
    --InstanceID aabbcc \
    --Host.Status 1 \
    --Host.Engine 1 \
    --Host.Domain 1 \
    --Host.DomainId 1 \
    --Host.LoadBalancerSet.0.Protocol 1 \
    --Host.LoadBalancerSet.0.Zone 1 \
    --Host.LoadBalancerSet.0.Region gz \
    --Host.LoadBalancerSet.0.LoadBalancerId 1 \
    --Host.LoadBalancerSet.0.ListenerId 1 \
    --Host.LoadBalancerSet.0.Vip 1 \
    --Host.LoadBalancerSet.0.ListenerName 1 \
    --Host.LoadBalancerSet.0.LoadBalancerName 1 \
    --Host.LoadBalancerSet.0.Vport 1 \
    --Host.Level 1 \
    --Host.MainDomain snv.vom \
    --Host.Region cd \
    --Host.FlowMode 1 \
    --Host.State 1 \
    --Host.ClsStatus 1 \
    --Host.IsCdn 1 \
    --Host.Mode 1 \
    --Host.Edition clb-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "97720395-7456-4a21-bcd9-1f32a7deaa90",
        "Error": {
            "Code": "ResourceInUse",
            "Message": "DomainExisted"
        }
    }
}
```

