**Example 1: 设置负载均衡的安全组**



Input: 

```
tccli ecm SetLoadBalancerSecurityGroups --cli-unfold-argument  \
    --LoadBalancerId lb-mov2697v \
    --SecurityGroups esg-0t3h9lmk
```

Output: 
```
{
    "Response": {
        "RequestId": "88487432-ee86-4e5d-861b-774374123f89"
    }
}
```

