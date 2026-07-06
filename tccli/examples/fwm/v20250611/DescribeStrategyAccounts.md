**Example 1: 查询防火墙管理规则下发账号**



Input: 

```
tccli fwm DescribeStrategyAccounts --cli-unfold-argument  \
    --Product enterprise_sg
```

Output: 
```
{
    "Response": {
        "AccountGroups": [
            {
                "BottleneckUin": "100011949846",
                "DispatchRuleNum": 0,
                "GroupId": "acg-dudjfm6t",
                "GroupName": "测试1",
                "MemberCount": 3,
                "Members": [
                    {
                        "DispatchRuleNum": 0,
                        "MemberId": "mem-1300846651-100011949846",
                        "Nickname": "焦糖小蛋糕",
                        "OriginRuleNum": 0,
                        "RemainQuota": 0,
                        "TotalQuota": 0,
                        "Uin": "100011949846"
                    },
                    {
                        "DispatchRuleNum": 0,
                        "MemberId": "mem-1300846651-100028354982",
                        "Nickname": "少年时",
                        "OriginRuleNum": 0,
                        "RemainQuota": 0,
                        "TotalQuota": 0,
                        "Uin": "100028354982"
                    },
                    {
                        "DispatchRuleNum": 0,
                        "MemberId": "mem-1300846651-100037509558",
                        "Nickname": "fengqqian",
                        "OriginRuleNum": 0,
                        "RemainQuota": 0,
                        "TotalQuota": 0,
                        "Uin": "100037509558"
                    }
                ],
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0
            },
            {
                "BottleneckUin": "100028671395",
                "DispatchRuleNum": 0,
                "GroupId": "acg-ssbkqes9",
                "GroupName": "生产测试组",
                "MemberCount": 1,
                "Members": [
                    {
                        "DispatchRuleNum": 0,
                        "MemberId": "mem-1300846651-100028671395",
                        "Nickname": "美式",
                        "OriginRuleNum": 0,
                        "RemainQuota": 0,
                        "TotalQuota": 0,
                        "Uin": "100028671395"
                    }
                ],
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0
            },
            {
                "BottleneckUin": "",
                "DispatchRuleNum": 0,
                "GroupId": "acg-na4l82l3",
                "GroupName": "测试2",
                "MemberCount": 0,
                "Members": [],
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0
            },
            {
                "BottleneckUin": "",
                "DispatchRuleNum": 0,
                "GroupId": "acg-uvrarqih",
                "GroupName": "<img src='' onerror='alert(\"cdasd\")' />",
                "MemberCount": 0,
                "Members": [],
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0
            }
        ],
        "Accounts": [
            {
                "DispatchRuleNum": 0,
                "MemberId": "mem-1300846651-100027980407",
                "Nickname": "2468639187",
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0,
                "Uin": "100027980407"
            },
            {
                "DispatchRuleNum": 0,
                "MemberId": "mem-1300846651-100028354982",
                "Nickname": "少年时",
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0,
                "Uin": "100028354982"
            },
            {
                "DispatchRuleNum": 0,
                "MemberId": "mem-1300846651-100028671395",
                "Nickname": "美式",
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0,
                "Uin": "100028671395"
            },
            {
                "DispatchRuleNum": 0,
                "MemberId": "mem-1300846651-100037509558",
                "Nickname": "fengqqian",
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0,
                "Uin": "100037509558"
            },
            {
                "DispatchRuleNum": 0,
                "MemberId": "mem-1300846651-100011949846",
                "Nickname": "焦糖小蛋糕",
                "OriginRuleNum": 0,
                "RemainQuota": 0,
                "TotalQuota": 0,
                "Uin": "100011949846"
            },
            {
                "DispatchRuleNum": 0,
                "MemberId": "mem-1300846651-100011616646",
                "Nickname": "天空之蓝",
                "OriginRuleNum": 17,
                "RemainQuota": 1983,
                "TotalQuota": 2000,
                "Uin": "100011616646"
            }
        ],
        "RequestId": "4b6c5bd5-c696-4ce8-a4c0-be583552aaaa"
    }
}
```

