**Example 1: 创建云联网策略路由匹配规则**



Input: 

```
tccli vpc CreateCcnPolicyBasedRoutingRules --cli-unfold-argument  \
    --CcnId ccn-cop4h86j \
    --CcnPolicyBasedRoutingRuleSet.0.InstanceType VPC \
    --CcnPolicyBasedRoutingRuleSet.0.InstanceId vpc-hj0u9uv7 \
    --CcnPolicyBasedRoutingRuleSet.0.PolicyBasedRoutingNextHopId pbrnh-7coeebmp \
    --CcnPolicyBasedRoutingRuleSet.0.SourceCidrBlock 10.0.0.0/16 \
    --CcnPolicyBasedRoutingRuleSet.0.DestinationCidrBlock 192.168.0.0/16 \
    --CcnPolicyBasedRoutingRuleSet.0.Priority 111 \
    --CcnPolicyBasedRoutingRuleSet.0.Description pbr-desc
```

Output: 
```
{
    "Response": {
        "PolicyBasedRoutingRuleIdSet": [
            "pbrrule-h80ym58o"
        ],
        "RequestId": "de080ffb-d39e-4510-94d0-452c825e4b5c"
    }
}
```

