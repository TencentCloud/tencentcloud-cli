**Example 1: Adding SNAT IP**



Input: 

```
tccli clb CreateLoadBalancerSnatIps --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --SnatIps.0.SubnetId subnet-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "898b431c-2745-4b27-80f6-e6e8038a0683"
    }
}
```

