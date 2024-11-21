**Example 1: Waf  CC V2 Upsert接口**



Input: 

```
tccli waf UpsertCCRule --cli-unfold-argument  \
    --Status 0 \
    --Advance 0 \
    --Domain test.com \
    --Name test2 \
    --Url /test \
    --Priority 50 \
    --Interval 60 \
    --MatchFunc 0 \
    --ValidTime 600
 \
    --Limit 60 \
    --ActionType 22 \
    --OptionsArr [{"key":"get","args":["a=12"]}]
```

Output: 
```
{
    "Response": {
        "Data": "success",
        "RequestId": "5029e2b0-493c-4dcc-9e4e-d53ab98ede99"
    }
}
```

