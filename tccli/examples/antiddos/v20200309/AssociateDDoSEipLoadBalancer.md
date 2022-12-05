**Example 1: 绑定高防弹性公网IP到负载均衡上**



Input: 

```
tccli antiddos AssociateDDoSEipLoadBalancer --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --Eip 1.1.1.1 \
    --Vip 1.1.1.1 \
    --LoadBalancerRegion ap-hongkong \
    --LoadBalancerID lb-0000002i
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

