**Example 1: ReplaceCcnRouteTableInputPolicys**

替换路由表接收策略

Input: 

```
tccli vpc ReplaceCcnRouteTableInputPolicys --cli-unfold-argument  \
    --CcnId ccn-rxz9krjj \
    --RouteTableId ccnrtb-63ujxv2h \
    --Policys.0.RouteConditions.0.Name instance-type \
    --Policys.0.RouteConditions.0.Values VPNGW \
    --Policys.0.RouteConditions.0.MatchPattern 1 \
    --Policys.0.Action accept \
    --Policys.0.Description 
```

Output: 
```
{
    "Response": {
        "RequestId": "82f40ff4-5ecf-4d7a-8081-18a652f38728"
    }
}
```

