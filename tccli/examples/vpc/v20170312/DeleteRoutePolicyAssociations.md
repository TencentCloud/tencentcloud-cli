**Example 1: 删除路由接收策略绑定**

删除路由接收策略绑定。

Input: 

```
tccli vpc DeleteRoutePolicyAssociations --cli-unfold-argument  \
    --RoutePolicyAssociationSet.0.RouteTableId rtb-qk8eyn9g \
    --RoutePolicyAssociationSet.0.RoutePolicyId rrp-q7ywkx3w \
    --RoutePolicyAssociationSet.0.Priority 100
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

