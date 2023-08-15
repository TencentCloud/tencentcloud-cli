**Example 1: 修改负载均衡所属项目**



Input: 

```
tccli clb ModifyLoadBalancersProject --cli-unfold-argument  \
    --LoadBalancerIds lb-1234abcd lb-5678wwqq \
    --ProjectId 1122
```

Output: 
```
{
    "Response": {
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba11"
    }
}
```

