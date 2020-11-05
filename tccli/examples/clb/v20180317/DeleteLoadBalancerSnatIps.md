**Example 1: Deleting SNAT IP**



Input: 

```
tccli clb DeleteLoadBalancerSnatIps --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --Ips 192.168.0.128
```

Output: 
```
{
    "Response": {
        "RequestId": "898b431c-2745-4b27-80f6-e6e8038a0683"
    }
}
```

