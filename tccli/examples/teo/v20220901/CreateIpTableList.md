**Example 1: 新建一条拦截名单**



Input: 

```
tccli teo CreateIpTableList --cli-unfold-argument  \
    --IpTableRules.0.Action drop \
    --IpTableRules.0.MatchFrom ip \
    --IpTableRules.0.UpdateTime 2020-09-22T00:00:00+00:00 \
    --IpTableRules.0.MatchContent 1.1.1.1 \
    --IpTableRules.0.RuleID 0 \
    --Entity a.eotest.com \
    --ZoneId zone-285thql0vdhi
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-xxxx-27cb34dac669"
    }
}
```

