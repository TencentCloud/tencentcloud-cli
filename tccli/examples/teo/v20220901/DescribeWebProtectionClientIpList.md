**Example 1: 查询CC防护客户端ip信息列表**



Input: 

```
tccli teo DescribeWebProtectionClientIpList --cli-unfold-argument  \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --Limit 1 \
    --Offset 1 \
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
        "TotalCount": 1,
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "Data": [
            {
                "ClientIp": "1.2.3.4",
                "RequestMaxQps": 10,
                "RequestNum": 10
            }
        ]
    }
}
```

