**Example 1: 查询bot攻击客户端ip信息列表**



Input: 

```
tccli teo DescribeBotClientIpList --cli-unfold-argument  \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --Limit 10 \
    --Offset 0 \
    --Interval min \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 20,
        "RequestId": "3824cf60-c2aa-4f4a-95b7-a4d5e4dee188",
        "Data": [
            {
                "ClientIp": "1.2.3.4",
                "RequestMaxQps": 100,
                "RequestNum": 100
            }
        ]
    }
}
```

