**Example 1: Waf  CC V2 Query接口  无数据返回场景**



Input: 

```
tccli waf DescribeCCRule --cli-unfold-argument  \
    --Domain www.test.com \
    --Limit 10 \
    --Offset 0 \
    --Edition clb-waf \
    --Sort priority:1;ts_version:-1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [],
            "TotalCount": 0
        },
        "RequestId": "b22fc98c-6c4f-4716-b043-f11ccbffde70"
    }
}
```

**Example 2: Waf  CC V2 Query接口  有数据返回场景**



Input: 

```
tccli waf DescribeCCRule --cli-unfold-argument  \
    --Domain test.com \
    --Limit 10 \
    --Offset 0 \
    --Edition clb-waf \
    --Sort priority:1;ts_version:-1
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
                    "OptionsArr": "[{\"key\":\"get\",\"args\":[\"=\"]}]",
                    "Priority": 50,
                    "Status": 1,
                    "TsVersion": 1579058116920,
                    "Url": "///",
                    "ValidTime": 600
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "1cc54bf4-cfeb-40cc-a823-035e52106df9"
    }
}
```

