**Example 1: 删除转发规则**



Input: 

```
tccli alb DeleteRules --cli-unfold-argument  \
    --ListenerId lst-d9p3k7wa \
    --LoadBalancerId alb-f8q2xk9m \
    --RuleIds rule-h8cy5gwl
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

