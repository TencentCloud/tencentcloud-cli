**Example 1: 删除日志服务主题**

删除负载均衡的日志服务(CLS)主题

Input: 

```
tccli clb SetLoadBalancerClsLog --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00 \
    --LogSetId  \
    --LogTopicId 
```

Output: 
```
{
    "Response": {
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

**Example 2: 设置日志服务主题**

添加，或修改负载均衡的日志服务(CLS)主题

Input: 

```
tccli clb SetLoadBalancerClsLog --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2r00 \
    --LogSetId ac251c08-778c-4fbc-981b-4898dd48d928 \
    --LogTopicId f43636fe-06fc-417b-9349-da4bc8a03745
```

Output: 
```
{
    "Response": {
        "RequestId": "78a40898-8210-44c7-8bc6-f83e50878d12"
    }
}
```

