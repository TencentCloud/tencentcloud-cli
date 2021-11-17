**Example 1: 添加SnatIp**



Input: 

```
tccli clb CreateLoadBalancerSnatIps --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw**** \
    --SnatIps.0.SubnetId subnet-1234**** \
    --Number 2
```

Output: 
```
{
    "Response": {
        "RequestId": "898b431c-2745-4b27-80f6-e6e8038a0683"
    }
}
```

**Example 2: 指定snat ip添加SnatIp**



Input: 

```
tccli clb CreateLoadBalancerSnatIps --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw**** \
    --SnatIps.0.SubnetId subnet-1234**** \
    --SnatIps.0.Ip 192.168.1.2
```

Output: 
```
{
    "Response": {
        "RequestId": "898b431c-80f6-80f6-80f6-e6e8038a0683"
    }
}
```

