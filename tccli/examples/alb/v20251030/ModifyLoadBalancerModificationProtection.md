**Example 1: 设置负载均衡实例操作保护**



Input: 

```
tccli alb ModifyLoadBalancerModificationProtection --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --ModificationProtectionEnabled True \
    --Reason prod_protection
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

