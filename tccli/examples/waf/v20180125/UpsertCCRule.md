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
        "Data": null,
        "RequestId": "5029e2b0-493c-4dcc-9e4e-d53ab98ede99"
    }
}
```

**Example 2: test**



Input: 

```
tccli waf UpsertCCRule --cli-unfold-argument  \
    --Status 0 \
    --MatchFunc 0 \
    --Domain hzh.qcloud.com \
    --Name ddp \
    --Advance 0 \
    --ValidTime 61 \
    --Interval 10 \
    --Priority 1 \
    --Url /test \
    --Limit 10 \
    --ActionType 20
```

Output: 
```
{
    "Response": {
        "RequestId": "2ca5c6bb-05b7-4183-bbf2-3c7059544317",
        "Data": ""
    }
}
```

**Example 3: test1**



Input: 

```
tccli waf UpsertCCRule --cli-unfold-argument  \
    --Status 0 \
    --MatchFunc 0 \
    --Domain hzh.qcloud.com \
    --Name ddp \
    --Advance 0 \
    --ValidTime 61 \
    --Interval 10 \
    --Priority 1 \
    --Url /test \
    --Limit 10 \
    --ActionType 20
```

Output: 
```
{
    "Response": {
        "RequestId": "2ca5c6bb-05b7-4183-bbf2-3c7059544317",
        "Data": ""
    }
}
```

