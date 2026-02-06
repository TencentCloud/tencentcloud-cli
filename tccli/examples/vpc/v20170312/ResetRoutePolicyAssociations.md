**Example 1: 重置路由策略绑定**

重置路由策略绑定。

Input: 

```
tccli vpc ResetRoutePolicyAssociations --cli-unfold-argument  \
    --RoutePolicyAssociationSet.0.RouteTableId rtb-cinupu2w \
    --RoutePolicyAssociationSet.0.RoutePolicyId rrp-q7ywkx3w \
    --RoutePolicyAssociationSet.0.Priority 100 \
    --RouteTableId rtb-cinupu2w
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

