**Example 1: 攻击日志统计详情**



Input: 

```
tccli waf GetAttackHistogram --cli-unfold-argument  \
    --Domain waf.com \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --QueryString bot:0
```

Output: 
```
{
    "Response": {
        "RequestId": "977c060f-4db5-4a48-95a1-bc4c7b141276",
        "Data": [
            {
                "Count": 0,
                "TimeStamp": 1598544000
            },
            {
                "Count": 0,
                "TimeStamp": 1598545800
            },
            {
                "Count": 0,
                "TimeStamp": 1598547600
            },
            {
                "Count": 0,
                "TimeStamp": 1598549400
            },
            {
                "Count": 0,
                "TimeStamp": 1598551200
            },
            {
                "Count": 0,
                "TimeStamp": 1598553000
            },
            {
                "Count": 0,
                "TimeStamp": 1598554800
            },
            {
                "Count": 0,
                "TimeStamp": 1598556600
            },
            {
                "Count": 0,
                "TimeStamp": 1598558400
            },
            {
                "Count": 0,
                "TimeStamp": 1598560200
            },
            {
                "Count": 0,
                "TimeStamp": 1598562000
            },
            {
                "Count": 0,
                "TimeStamp": 1598563800
            },
            {
                "Count": 0,
                "TimeStamp": 1598565600
            },
            {
                "Count": 0,
                "TimeStamp": 1598567400
            },
            {
                "Count": 0,
                "TimeStamp": 1598569200
            },
            {
                "Count": 0,
                "TimeStamp": 1598571000
            },
            {
                "Count": 0,
                "TimeStamp": 1598572800
            },
            {
                "Count": 0,
                "TimeStamp": 1598574600
            },
            {
                "Count": 0,
                "TimeStamp": 1598576400
            },
            {
                "Count": 0,
                "TimeStamp": 1598578200
            },
            {
                "Count": 0,
                "TimeStamp": 1598580000
            },
            {
                "Count": 0,
                "TimeStamp": 1598581800
            },
            {
                "Count": 17,
                "TimeStamp": 1598583600
            },
            {
                "Count": 0,
                "TimeStamp": 1598585400
            },
            {
                "Count": 0,
                "TimeStamp": 1598587200
            },
            {
                "Count": 0,
                "TimeStamp": 1598589000
            },
            {
                "Count": 0,
                "TimeStamp": 1598590800
            },
            {
                "Count": 0,
                "TimeStamp": 1598592600
            },
            {
                "Count": 0,
                "TimeStamp": 1598594400
            }
        ],
        "Period": 1800,
        "TotalCount": 17
    }
}
```

