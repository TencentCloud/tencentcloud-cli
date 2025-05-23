**Example 1: 添加负载均衡型WAF域名**



Input: 

```
tccli waf CreateHost --cli-unfold-argument  \
    --InstanceID waf_2kzgm331pk3213 \
    --Host.Status 1 \
    --Host.Engine 1 \
    --Host.Domain lucainfo.qcloudwaf.com \
    --Host.DomainId waf-d4foqwZy \
    --Host.LoadBalancerSet.0.Protocol HTTP \
    --Host.LoadBalancerSet.0.Zone 1 \
    --Host.LoadBalancerSet.0.Region gz \
    --Host.LoadBalancerSet.0.LoadBalancerName 门户 \
    --Host.LoadBalancerSet.0.ListenerId lbl-87vxk72 \
    --Host.LoadBalancerSet.0.Vip 127.0.0.1 \
    --Host.LoadBalancerSet.0.ListenerName 监听器测试 \
    --Host.LoadBalancerSet.0.LoadBalancerId lb-2s7f791x \
    --Host.LoadBalancerSet.0.Vport 80 \
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

**Example 2: 添加内网负载均衡型WAF域名**



Input: 

```
tccli waf CreateHost --cli-unfold-argument  \
    --InstanceID waf_2kzgm331pk3213 \
    --Host.Status 1 \
    --Host.Engine 1 \
    --Host.Domain lucainfointer.qcloudwaf.com \
    --Host.DomainId waf-d4foqwZy \
    --Host.LoadBalancerSet.0.Protocol HTTP \
    --Host.LoadBalancerSet.0.Zone  \
    --Host.LoadBalancerSet.0.Region gz \
    --Host.LoadBalancerSet.0.LoadBalancerName 门户 \
    --Host.LoadBalancerSet.0.ListenerId lbl-87vxk85 \
    --Host.LoadBalancerSet.0.Vip 172.16.49.53 \
    --Host.LoadBalancerSet.0.ListenerName 监听器测试 \
    --Host.LoadBalancerSet.0.LoadBalancerId lb-2s7f123 \
    --Host.LoadBalancerSet.0.Vport 80 \
    --Host.LoadBalancerSet.0.LoadBalancerType INTERNAL \
    --Host.LoadBalancerSet.0.NumericalVpcId 11533948 \
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
        "DomainId": "waf-cr3rPnlN",
        "RequestId": "0c93baaf-d7b8-4ab8-8d91-759128d5d864"
    }
}
```

