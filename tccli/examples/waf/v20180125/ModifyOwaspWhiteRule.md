**Example 1: 修改规则白名单**



Input: 

```
tccli waf ModifyOwaspWhiteRule --cli-unfold-argument  \
    --RuleId 10000 \
    --Name 测试白名单 \
    --Domain owasp.saas3.testwaf.com \
    --Strategies.0.Field IP \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Content 1.1.1.1 \
    --Strategies.0.Arg GET \
    --Strategies.0.CaseNotSensitive 1 \
    --Ids 10000 \
    --Type 1 \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 0 \
    --JobDateTime.Timed.0.EndDateTime 0 \
    --JobDateTime.Cron.0.StartTime 0 \
    --JobDateTime.Cron.0.EndTime 0 \
    --JobDateTime.TimeTZone UTC+8	 \
    --ExpireTime 0 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e1955c61-d2de-40e2-a084-8fdfa871ceec"
    }
}
```

