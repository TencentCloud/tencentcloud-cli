**Example 1: 将实例类型修改为内网**



Input: 

```
tccli alb ModifyLoadBalancerAddressType --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --AddressType Intranet
```

Output: 
```
{
    "Response": {
        "RequestId": "a44ec7d9-94ce-4c45-8fb0-bab95dbb5122"
    }
}
```

