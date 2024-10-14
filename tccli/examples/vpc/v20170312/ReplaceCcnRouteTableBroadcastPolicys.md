**Example 1: 替换云联网路由传播策略**

替换云联网路由传播策略

Input: 

```
tccli vpc ReplaceCcnRouteTableBroadcastPolicys --cli-unfold-argument  \
    --CcnId ccn-qd6z2ld1 \
    --RouteTableId ccnrtb-1mkezrkd \
    --Policys.0.RouteConditions.0.Name instance-type \
    --Policys.0.RouteConditions.0.Values VPC DIRECTCONNECT \
    --Policys.0.RouteConditions.0.MatchPattern 1 \
    --Policys.0.RouteConditions.1.Name instance-id \
    --Policys.0.RouteConditions.1.Values dcg-8zljkrft vpc-jdevjrup \
    --Policys.0.RouteConditions.1.MatchPattern 1 \
    --Policys.0.BroadcastConditions.0.Name instance-id \
    --Policys.0.BroadcastConditions.0.Values vpc-jdevjrup vpc-hb81v349 \
    --Policys.0.BroadcastConditions.0.MatchPattern 1 \
    --Policys.0.Action accept \
    --Policys.0.Description 指定vpc接收北京指定专线和vpc路由 \
    --Policys.1.RouteConditions.0.Name instance-region \
    --Policys.1.RouteConditions.0.Values ap-beijing \
    --Policys.1.RouteConditions.0.MatchPattern 1 \
    --Policys.1.RouteConditions.1.Name instance-type \
    --Policys.1.RouteConditions.1.Values VPC DIRECTCONNECT VPNGW \
    --Policys.1.RouteConditions.1.MatchPattern 1 \
    --Policys.1.RouteConditions.2.Name cidr-block \
    --Policys.1.RouteConditions.2.Values 9.0.0.0/8 10.0.0.0/8 192.168.0.0/24 \
    --Policys.1.RouteConditions.2.MatchPattern 1 \
    --Policys.1.BroadcastConditions.0.Name instance-region \
    --Policys.1.BroadcastConditions.0.Values ap-beijing \
    --Policys.1.BroadcastConditions.0.MatchPattern 1 \
    --Policys.1.BroadcastConditions.1.Name instance-id \
    --Policys.1.BroadcastConditions.1.Values vpc-jdevjrup vpc-hb81v349 \
    --Policys.1.BroadcastConditions.1.MatchPattern 1 \
    --Policys.1.Action drop \
    --Policys.1.Description 指定VPC绝收北京地域专线、VPC、VPN三大网段
```

Output: 
```
{
    "Response": {
        "RequestId": "6fe64d7f-3983-4f17-847d-a60dded41951"
    }
}
```

