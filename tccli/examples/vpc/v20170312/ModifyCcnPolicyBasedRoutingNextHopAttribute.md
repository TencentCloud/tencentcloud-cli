**Example 1: 更新云联网策略路由下一跳参数**



Input: 

```
tccli vpc ModifyCcnPolicyBasedRoutingNextHopAttribute --cli-unfold-argument  \
    --CcnId ccn-cop4h86j \
    --PolicyBasedRoutingNextHopId pbrnh-hows4a7d \
    --Name test2222 \
    --State DISABLE
```

Output: 
```
{
    "Response": {
        "RequestId": "dc3f9101-29bd-4749-9438-e5c70f6f248a"
    }
}
```

