**Example 1: 修改黑石负载均衡七层转发路径**



Input: 

```
tccli bmlb ModifyL7Locations --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --RuleSet.0.DomainId dm-hg8j52ud \
    --RuleSet.0.LocationId loc-02ywyc8b \
    --RuleSet.0.Url /a/b/c/ \
    --RuleSet.0.SessionExpire 100 \
    --RuleSet.0.HealthSwitch 1 \
    --RuleSet.0.IntervalTime 99 \
    --RuleSet.0.HealthNum 5 \
    --RuleSet.0.UnhealthNum 6 \
    --RuleSet.0.HttpCodes 2 \
    --RuleSet.0.HttpCheckPath /b/ \
    --RuleSet.0.HttpCheckDomain b.com \
    --RuleSet.0.BalanceMode wrr
```

Output: 
```
{
    "Response": {
        "TaskId": 2385737,
        "RequestId": "e8ad93b1-d2c9-430a-ae3b-108ba39571ec"
    }
}
```

