**Example 1: test1**



Input: 

```
tccli waf DescribeCCRuleList --cli-unfold-argument  \
    --By ts_version \
    --Domain hzh.qcloud.com \
    --Limit 10 \
    --Order asc \
    --Offset 10000002
```

Output: 
```
{
    "Response": {
        "RequestId": "41b55f8b-1ed1-484c-aab7-c14c0889f78b",
        "Data": {
            "Res": [
                {
                    "Name": "test",
                    "Status": 0,
                    "Advance": 0,
                    "Limit": 2,
                    "Interval": 60,
                    "Url": "/",
                    "MatchFunc": 0,
                    "ActionType": 22,
                    "Priority": 50,
                    "ValidTime": 600,
                    "TsVersion": 1609769256761,
                    "Options": "[]",
                    "RuleId": 0,
                    "EventId": "11"
                },
                {
                    "Name": "ddp",
                    "Status": 0,
                    "Advance": 0,
                    "Limit": 10,
                    "Interval": 10,
                    "Url": "/test",
                    "MatchFunc": 0,
                    "ActionType": 20,
                    "Priority": 1,
                    "ValidTime": 61,
                    "TsVersion": 1669794335102,
                    "Options": "",
                    "RuleId": 1900009616,
                    "EventId": "111"
                }
            ],
            "TotalCount": 2
        }
    }
}
```

**Example 2: 根据URL查询API规则**



Input: 

```
tccli waf DescribeCCRuleList --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Limit 1 \
    --Filters.0.Values clb saas \
    --Filters.0.Name InstanceType \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --By ts_version
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "ActionType": 22,
                    "Advance": 0,
                    "Interval": 60,
                    "Limit": 60,
                    "MatchFunc": 0,
                    "Name": "test1",
                    "Priority": 50,
                    "Status": 1,
                    "TsVersion": 1579058116920,
                    "Url": "///",
                    "ValidTime": 600,
                    "Options": "",
                    "RuleId": 1900009616,
                    "EventId": "111"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "1cc54bf4-cfeb-40cc-a823-035e52106df9"
    }
}
```

