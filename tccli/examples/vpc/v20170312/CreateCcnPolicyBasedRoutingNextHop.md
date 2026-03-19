**Example 1: 创建云联网策略路由下一跳**



Input: 

```
tccli vpc CreateCcnPolicyBasedRoutingNextHop --cli-unfold-argument  \
    --InstanceType VPC \
    --InstanceId vpc-hj0u9uv7 \
    --CcnId ccn-cop4h86j \
    --NextHopResourceType HAVIP \
    --NextHopResourceId havip-lmojafue \
    --NextHopRegion ap-guangzhou \
    --Name pbr-next-hop-1 \
    --State ENABLE
```

Output: 
```
{
    "Response": {
        "PolicyBasedRoutingNextHopId": "pbrnh-dqr4ouw5",
        "RequestId": "e50fc6f8-628a-4ab8-a441-d8772cd1f6f3"
    }
}
```

