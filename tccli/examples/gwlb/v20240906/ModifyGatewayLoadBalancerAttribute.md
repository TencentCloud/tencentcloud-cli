**Example 1: 修改网关负载均衡实例名称**

修改网关负载均衡实例名称

Input: 

```
tccli gwlb ModifyGatewayLoadBalancerAttribute --cli-unfold-argument  \
    --LoadBalancerId gwlb-6efswuxa \
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

