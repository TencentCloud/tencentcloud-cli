**Example 1: 新建cc规则示例**



Input: 

```
tccli waf UpsertCCRule --cli-unfold-argument  \
    --Domain yyxz.1030.testwaf.com \
    --Name 测试使用 \
    --Status 1 \
    --Advance 0 \
    --Limit 60 \
    --Interval 60 \
    --ActionType 22 \
    --Priority 50 \
    --ValidTime 600 \
    --Url  \
    --MatchFunc 0 \
    --OptionsArr [{"key":"URL","args":["=L2NjdGVzdA"],"match":"0","encodeflag":true}] \
    --Edition sparta-waf \
    --Type 0 \
    --EventId  \
    --RuleId 0 \
    --LimitMethod  \
    --CelRule  \
    --LogicalOp and \
    --PageId  \
    --ActionRatio 100 \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 1769529600 \
    --JobDateTime.Timed.0.EndDateTime 1771776000 \
    --JobDateTime.TimeTZone UTC+8
```

Output: 
```
{
    "Response": {
        "Data": "",
        "RuleId": 0,
        "RequestId": "707d8c2c-413f-49b7-a03a-39aa61a07202"
    }
}
```

