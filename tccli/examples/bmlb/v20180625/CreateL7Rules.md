**Example 1: 创建黑石负载均衡七层转发规则**



Input: 

```
tccli bmlb CreateL7Rules --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --RuleSet.0.Domain b.com \
    --RuleSet.0.Url / \
    --RuleSet.0.SessionExpire 30 \
    --RuleSet.0.HealthSwitch 1 \
    --RuleSet.0.IntervalTime 30 \
    --RuleSet.0.HealthNum 3 \
    --RuleSet.0.UnhealthNum 4 \
    --RuleSet.0.HttpCodes 1 \
    --RuleSet.0.HttpCheckPath /a/ \
    --RuleSet.0.HttpCheckDomain b.com \
    --RuleSet.0.BalanceMode wrr
```

Output: 
```
{
    "Response": {
        "TaskId": 2385736,
        "RequestId": "2b0e4dc0-eaac-4a4c-bdd4-d3815aeaffeb"
    }
}
```

