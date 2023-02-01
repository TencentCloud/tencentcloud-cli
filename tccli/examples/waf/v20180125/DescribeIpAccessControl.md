**Example 1: Waf ip黑白名单查询**

Waf ip黑名单查询

Input: 

```
tccli waf DescribeIpAccessControl --cli-unfold-argument  \
    --Domain www.test.com \
    --Count 1 \
    --ActionType 42 \
    --Limit 20 \
    --OffSet 0 \
    --Sort ts_version:-1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "ActionType": 42,
                    "Ip": "1.1.1.1",
                    "Note": "",
                    "Source": "custom",
                    "TsVersion": 1579074751421,
                    "ValidTs": 1579017599
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "c937ce96-cf53-4df8-b288-07c6e092072d"
    }
}
```

