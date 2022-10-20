**Example 1: 查询漏洞防御攻击事件趋势**



Input: 

```
tccli tcss DescribeVulDefenceEventTendency --cli-unfold-argument  \
    --EndTime 2021-05-01 \
    --StartTime 2021-05-07
```

Output: 
```
{
    "Response": {
        "AttackList": [
            {
                "Date": "2020-09-22",
                "EventCount": 0
            }
        ],
        "RequestId": "xx",
        "DefendedList": [
            {
                "Date": "2020-09-22",
                "EventCount": 0
            }
        ]
    }
}
```

