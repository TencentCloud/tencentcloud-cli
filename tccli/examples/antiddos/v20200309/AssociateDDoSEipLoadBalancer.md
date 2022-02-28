**Example 1: 绑定高防弹性公网IP到负载均衡上**



Input: 

```
tccli antiddos AssociateDDoSEipLoadBalancer --cli-unfold-argument  \
    --InstanceId xx \
    --Eip xx \
    --Vip xx \
    --LoadBalancerRegion xx \
    --LoadBalancerID xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

