**Example 1: 创建仅DNS模式负载均衡**



Input: 

```
tccli teo CreateLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --Host test.tencent.com \
    --Type dns_only \
    --OriginGroupId orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a \
    --BackupOriginGroupId  \
    --TTL 600 \
    --OriginType normal
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "LoadBalancingId": "lb-97c8396e-cb88-4c9c-98d9-38e86463d12e"
    }
}
```

**Example 2: 创建开启代理模式负载均衡**



Input: 

```
tccli teo CreateLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --Host test.tencent.com \
    --Type proxied \
    --OriginGroupId orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a \
    --BackupOriginGroupId  \
    --OriginType normal
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "LoadBalancingId": "lb-97c8396e-cb88-4c9c-98d9-38e86463d12e"
    }
}
```

**Example 3: 创建使用备用源站的负载均衡**



Input: 

```
tccli teo CreateLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --Host test.tencent.com \
    --Type proxied \
    --OriginGroupId orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a \
    --BackupOriginGroupId orgin-9cc50b24-7dc5-44f4-96ce-95825d53ff2f \
    --OriginType normal
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "LoadBalancingId": "lb-97c8396e-cb88-4c9c-98d9-38e86463d12e"
    }
}
```

**Example 4: 创建使用高级源站配置的负载均衡**



Input: 

```
tccli teo CreateLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --Host test.tencent.com \
    --Type proxied \
    --OriginGroupId orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a \
    --BackupOriginGroupId orgin-9cc50b24-7dc5-44f4-96ce-95825d53ff2f \
    --OriginType advanced \
    --AdvancedOriginGroups.0.OriginGroupConditions.0.Target url \
    --AdvancedOriginGroups.0.OriginGroupConditions.0.Operator equal \
    --AdvancedOriginGroups.0.OriginGroupConditions.0.Values /image \
    --AdvancedOriginGroups.0.OriginGroupId orgin-9cc50b24-7dc5-44f4-96ce-95825d53ff2f \
    --AdvancedOriginGroups.0.BackupOriginGroupId 
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "LoadBalancingId": "lb-97c8396e-cb88-4c9c-98d9-38e86463d12e"
    }
}
```

