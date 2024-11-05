**Example 1: 编辑负载均衡型WAF域名**



Input: 

```
tccli waf ModifyHost --cli-unfold-argument  \
    --Host.AlbType clb \
    --Host.DomainId waf-Lt6LGSlM \
    --Host.Domain txwafstar.qcloudwaf.com \
    --Host.MainDomain qlcloudwaf.com \
    --Host.Mode 1 \
    --Host.Status 1 \
    --Host.State 1 \
    --Host.Engine 1 \
    --Host.IsCdn 1 \
    --Host.ClsStatus 1 \
    --Host.Edition clb-waf \
    --Host.FlowMode 1 \
    --Host.LoadBalancerSet.0.LoadBalancerId waf-Lt6LGSlM \
    --Host.LoadBalancerSet.0.Protocol HTTP \
    --Host.LoadBalancerSet.0.NumericalVpcId 1140321 \
    --Host.LoadBalancerSet.0.LoadBalancerType OPEN \
    --Host.LoadBalancerSet.0.Zone ap-chengdu-2 \
    --Host.LoadBalancerSet.0.LoadBalancerName clbtest \
    --Host.LoadBalancerSet.0.ListenerId lbl-2k0gmnv1 \
    --Host.LoadBalancerSet.0.ListenerName http-443 \
    --Host.LoadBalancerSet.0.Vip 127.0.0.1 \
    --Host.LoadBalancerSet.0.Vport 443 \
    --Host.LoadBalancerSet.0.Region cd \
    --Host.Region cd
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

