**Example 1: 创建路由接收策略绑定**

创建路由接收策略绑定。

Input: 

```
tccli vpc CreateRoutePolicyAssociations --cli-unfold-argument  \
    --RoutePolicyAssociationSet.0.RouteTableId rtb-qk8eyn9g \
    --RoutePolicyAssociationSet.0.RoutePolicyId rrp-q7ywkx3w \
    --RoutePolicyAssociationSet.0.Priority 100
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

