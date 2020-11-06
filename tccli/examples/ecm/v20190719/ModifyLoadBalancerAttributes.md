**Example 1: 修改负载均衡实例的属性**



Input: 

```
tccli ecm ModifyLoadBalancerAttributes --cli-unfold-argument  \
    --LoadBalancerId lb-6efswuxa \
    --LoadBalancerName newlbname
```

Output: 
```
{
    "Response": {
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

