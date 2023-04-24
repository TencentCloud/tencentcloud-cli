**Example 1: 修改负载均衡实例名称**

修改负载均衡

Input: 

```
tccli clb ModifyLoadBalancerAttributes --cli-unfold-argument  \
    --LoadBalancerName newlbname \
    --LoadBalancerId lb-6efswuxa
```

Output: 
```
{
    "Response": {
        "DealName": null,
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

