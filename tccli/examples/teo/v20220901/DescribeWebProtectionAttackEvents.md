**Example 1: 查询DDos攻击事件**



Input: 

```
tccli teo DescribeWebProtectionAttackEvents --cli-unfold-argument  \
    --Domains dloc3.huolala.cn \
    --ZoneIds www.huolala.com \
    --StartTime 2022-01-10T16:01:00Z \
    --EndTime 2022-01-10T16:05:00Z \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "58bacbc7-b47b-435d-abf2-c98ca34be020",
        "Data": [
            {
                "ClientIp": "1.1.1.1",
                "InterceptNum": 20000,
                "InterceptTime": 1641801660
            },
            {
                "ClientIp": "1.1.1.1",
                "InterceptNum": 10000,
                "InterceptTime": 1641801660
            }
        ],
        "TotalCount": 2
    }
}
```

