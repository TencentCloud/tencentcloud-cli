**Example 1: 开启混绑IP功能**

开启混绑IP功能

Input: 

```
tccli clb ModifyLoadBalancerMixIpTarget --cli-unfold-argument  \
    --LoadBalancerIds lb-1234abcd lb-5678wwqq \
    --MixIpTarget true
```

Output: 
```
{
    "Response": {
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba11"
    }
}
```

