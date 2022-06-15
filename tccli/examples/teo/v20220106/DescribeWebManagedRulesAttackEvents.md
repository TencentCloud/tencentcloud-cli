**Example 1: 查询DDos攻击事件**



Input: 

```
tccli teo DescribeWebManagedRulesAttackEvents --cli-unfold-argument  \
    --PageNo 3 \
    --PageSize 1 \
    --PolicyIds 1 2 \
    --ZoneIds www.huolala.com \
    --StartTime 2022-01-10T16:01:00Z \
    --EndTime 2022-01-10T16:05:00Z \
    --IsShowDetail Y
```

Output: 
```
{
    "Response": {
        "RequestId": "ec73285b-033e-483e-ac38-2dacce32b7eb",
        "Data": {
            "List": [
                {
                    "AttackTime": 1641801840,
                    "AttackUrl": "/uri/demo",
                    "ClientIp": "1.1.1.1"
                },
                {
                    "AttackTime": 1641801720,
                    "AttackUrl": "/uri/demo",
                    "ClientIp": "1.1.1.1"
                }
            ],
            "PageNo": 1,
            "PageSize": 2,
            "Pages": 2,
            "TotalSize": 4
        },
        "Msg": "success",
        "Status": 0
    }
}
```

