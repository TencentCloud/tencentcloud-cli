**Example 1: 添加白名单**



Input: 

```
tccli waf CreateOwaspWhiteRule --cli-unfold-argument  \
    --Name 测试白名单 \
    --Domain owasp.saas3.testwaf.com \
    --Strategies.0.Field IP \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Content 1.1.1.1 \
    --Strategies.0.Arg GET \
    --Ids 16 \
    --Type 1 \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 0 \
    --JobDateTime.Timed.0.EndDateTime 0 \
    --JobDateTime.TimeTZone UTC+8	 \
    --ExpireTime 0 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RuleId": "23123145",
        "RequestId": "01006b52-0313-4771-83eb-968d7b592dfa"
    }
}
```

