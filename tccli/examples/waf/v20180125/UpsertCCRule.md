**Example 1: 添加CC规则**



Input: 

```
tccli waf UpsertCCRule --cli-unfold-argument  \
    --RuleId 0 \
    --Domain www.testwaf.com \
    --Edition sparta-waf \
    --Name ccrule \
    --Status 1 \
    --Advance 0 \
    --Limit 60 \
    --Type 0 \
    --Interval 60 \
    --Url  \
    --MatchFunc 0 \
    --ActionType 22 \
    --Priority 50 \
    --ValidTime 600 \
    --OptionsArr [{"key":"URL","args":["=L2Nj"],"match":"0","encodeflag":true}] \
    --EventId  \
    --LogicalOp and \
    --CelRule  \
    --LimitMethod  \
    --ActionRatio 100 \
    --PageId 
```

Output: 
```
{
    "Response": {
        "RequestId": "8fb2ee72-103d-4d0f-b583-6af98aa2f442",
        "Data": "",
        "RuleId": 1900037990
    }
}
```

