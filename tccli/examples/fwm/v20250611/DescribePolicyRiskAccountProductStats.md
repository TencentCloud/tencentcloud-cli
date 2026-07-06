**Example 1: 查询仅待整改**



Input: 

```
tccli fwm DescribePolicyRiskAccountProductStats --cli-unfold-argument  \
    --Filters.0.Name OnlyUntreated \
    --Filters.0.Values 1 \
    --Filters.0.OperatorType 7
```

Output: 
```
{
    "Response": {
        "AccountStats": [
            {
                "Member": {
                    "AppId": "1300448058",
                    "MemberId": "mem-1300846651-100011616646",
                    "Nickname": "天空之蓝",
                    "Uin": "100011616646"
                },
                "ProductStats": [
                    {
                        "IgnoredRiskCount": 55,
                        "LastCheckTime": "2026-03-26 15:29:52",
                        "PolicyCount": 1151,
                        "Product": "sg",
                        "ProductName": "安全组",
                        "RectifyRate": "0%",
                        "TotalRiskCount": 152,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 97
                    },
                    {
                        "IgnoredRiskCount": 0,
                        "LastCheckTime": "2026-03-09 19:42:49",
                        "PolicyCount": 34,
                        "Product": "enterprise_sg",
                        "ProductName": "企业安全组",
                        "RectifyRate": "0%",
                        "TotalRiskCount": 4,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 4
                    }
                ],
                "UntreatedRiskCount": 101
            }
        ],
        "RequestId": "d4f449f9-921c-43ad-a97a-edb27a2d685a",
        "TotalCount": 1
    }
}
```

**Example 2: 查询仅超时未体检**



Input: 

```
tccli fwm DescribePolicyRiskAccountProductStats --cli-unfold-argument  \
    --Filters.0.Name OnlyOverdue \
    --Filters.0.Values 1 \
    --Filters.0.OperatorType 7
```

Output: 
```
{
    "Response": {
        "AccountStats": [
            {
                "Member": {
                    "AppId": "1314503630",
                    "MemberId": "mem-1300846651-100027980407",
                    "Nickname": "测试部门",
                    "Uin": "100027980407"
                },
                "ProductStats": [],
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1300846651",
                    "MemberId": "mem-1300846651-100011949846",
                    "Nickname": "焦糖小蛋糕",
                    "Uin": "100011949846"
                },
                "ProductStats": [],
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1327492904",
                    "MemberId": "mem-1300846651-100037509558",
                    "Nickname": "fengqqian",
                    "Uin": "100037509558"
                },
                "ProductStats": [],
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1315399711",
                    "MemberId": "mem-1300846651-100028671395",
                    "Nickname": "美式",
                    "Uin": "100028671395"
                },
                "ProductStats": [],
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1314933167",
                    "MemberId": "mem-1300846651-100028354982",
                    "Nickname": "少年时",
                    "Uin": "100028354982"
                },
                "ProductStats": [],
                "UntreatedRiskCount": 0
            }
        ],
        "RequestId": "82758a29-81f8-466e-a8cd-ea60343d23fe",
        "TotalCount": 5
    }
}
```

**Example 3: 查询账号+产品维度风险统计**



Input: 

```
tccli fwm DescribePolicyRiskAccountProductStats --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AccountStats": [
            {
                "Member": {
                    "AppId": "1300448058",
                    "Uin": "100000009710",
                    "Nickname": "cfw-test",
                    "MemberId": "member-001"
                },
                "UntreatedRiskCount": 20,
                "ProductStats": [
                    {
                        "Product": "enterprise_sg",
                        "ProductName": "企业安全组",
                        "PolicyCount": 200,
                        "UntreatedRiskCount": 20,
                        "TotalRiskCount": 30,
                        "TreatedRiskCount": 5,
                        "IgnoredRiskCount": 5,
                        "RectifyRate": "0%",
                        "LastCheckTime": "2025-10-22 10:00:00"
                    },
                    {
                        "Product": "sg",
                        "ProductName": "安全组",
                        "PolicyCount": 100,
                        "UntreatedRiskCount": 0,
                        "TotalRiskCount": 0,
                        "TreatedRiskCount": 0,
                        "IgnoredRiskCount": 0,
                        "RectifyRate": "无需整改",
                        "LastCheckTime": "2025-10-22 10:00:00"
                    }
                ]
            },
            {
                "Member": {
                    "AppId": "1300846651",
                    "Uin": "100000009711",
                    "Nickname": "cfw-test2",
                    "MemberId": "member-002"
                },
                "UntreatedRiskCount": 1,
                "ProductStats": [
                    {
                        "Product": "sg",
                        "ProductName": "安全组",
                        "PolicyCount": 20,
                        "UntreatedRiskCount": 1,
                        "TotalRiskCount": 1,
                        "TreatedRiskCount": 0,
                        "IgnoredRiskCount": 0,
                        "RectifyRate": "0%",
                        "LastCheckTime": "2025-10-22 10:00:00"
                    }
                ]
            }
        ],
        "TotalCount": 2,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

**Example 4: 根据Uin过滤**



Input: 

```
tccli fwm DescribePolicyRiskAccountProductStats --cli-unfold-argument  \
    --Filters.0.Name Uin \
    --Filters.0.Values 100011616646 \
    --Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AccountStats": [
            {
                "Member": {
                    "AppId": "1300448058",
                    "MemberId": "mem-1300846651-100011616646",
                    "Nickname": "天空之蓝",
                    "Uin": "100011616646"
                },
                "ProductStats": [
                    {
                        "IgnoredRiskCount": 55,
                        "LastCheckTime": "2026-03-26 15:29:52",
                        "PolicyCount": 1151,
                        "Product": "sg",
                        "ProductName": "安全组",
                        "RectifyRate": "0%",
                        "TotalRiskCount": 152,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 97
                    },
                    {
                        "IgnoredRiskCount": 0,
                        "LastCheckTime": "2026-03-09 19:42:49",
                        "PolicyCount": 34,
                        "Product": "enterprise_sg",
                        "ProductName": "企业安全组",
                        "RectifyRate": "0%",
                        "TotalRiskCount": 4,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 4
                    }
                ],
                "UntreatedRiskCount": 101
            }
        ],
        "RequestId": "de07ff51-a85e-4970-883a-0b73f788eb06",
        "TotalCount": 1
    }
}
```

**Example 5: 根据账号昵称筛选**



Input: 

```
tccli fwm DescribePolicyRiskAccountProductStats --cli-unfold-argument  \
    --Filters.0.Name Nickname \
    --Filters.0.Values 蓝 \
    --Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AccountStats": [
            {
                "Member": {
                    "AppId": "1300448058",
                    "MemberId": "mem-1300846651-100011616646",
                    "Nickname": "天空之蓝",
                    "Uin": "100011616646"
                },
                "ProductStats": [
                    {
                        "IgnoredRiskCount": 55,
                        "LastCheckTime": "2026-03-26 15:29:52",
                        "PolicyCount": 1151,
                        "Product": "sg",
                        "ProductName": "安全组",
                        "RectifyRate": "0%",
                        "TotalRiskCount": 152,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 97
                    },
                    {
                        "IgnoredRiskCount": 0,
                        "LastCheckTime": "2026-03-09 19:42:49",
                        "PolicyCount": 34,
                        "Product": "enterprise_sg",
                        "ProductName": "企业安全组",
                        "RectifyRate": "0%",
                        "TotalRiskCount": 4,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 4
                    }
                ],
                "UntreatedRiskCount": 101
            }
        ],
        "RequestId": "09c2396d-5a7f-4d0b-b54d-eaa11f0729f1",
        "TotalCount": 1
    }
}
```

**Example 6: 默认请求**



Input: 

```
tccli fwm DescribePolicyRiskAccountProductStats --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccountStats": [
            {
                "Member": {
                    "AppId": "1300448058",
                    "MemberId": "mem-1300846651-100011616646",
                    "Nickname": "天空之蓝",
                    "Uin": "100011616646"
                },
                "ProductStats": [
                    {
                        "IgnoredRiskCount": 55,
                        "IsOverdue": true,
                        "LastCheckTime": "2026-03-26 15:29:52",
                        "PolicyCount": 1151,
                        "Product": "sg",
                        "ProductName": "安全组",
                        "RectifyRate": "0%",
                        "SubcategoryIds": [
                            "risk_port_ssh_22",
                            "inbound_accept_any",
                            "exact_duplicate_rules",
                            "merge_rules",
                            "risk_port_rdp_3389",
                            "risk_port_20_21",
                            "overridden_rules"
                        ],
                        "TotalRiskCount": 152,
                        "TreatedRiskCount": 0,
                        "UntreatedRiskCount": 97
                    },
                    {
                        "IgnoredRiskCount": 0,
                        "IsOverdue": true,
                        "LastCheckTime": "2026-03-27 11:47:27",
                        "PolicyCount": 46,
                        "Product": "enterprise_sg",
                        "ProductName": "企业安全组",
                        "RectifyRate": "无需整改",
                        "SubcategoryIds": [],
                        "TotalRiskCount": 24,
                        "TreatedRiskCount": 24,
                        "UntreatedRiskCount": 0
                    }
                ],
                "RectifyRate": "14%",
                "UntreatedRiskCount": 97
            },
            {
                "Member": {
                    "AppId": "1300846651",
                    "MemberId": "mem-1300846651-100011949846",
                    "Nickname": "焦糖小蛋糕",
                    "Uin": "100011949846"
                },
                "ProductStats": [],
                "RectifyRate": "无需整改",
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1327492904",
                    "MemberId": "mem-1300846651-100037509558",
                    "Nickname": "fengqqian",
                    "Uin": "100037509558"
                },
                "ProductStats": [],
                "RectifyRate": "无需整改",
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1315399711",
                    "MemberId": "mem-1300846651-100028671395",
                    "Nickname": "美式",
                    "Uin": "100028671395"
                },
                "ProductStats": [],
                "RectifyRate": "无需整改",
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1314933167",
                    "MemberId": "mem-1300846651-100028354982",
                    "Nickname": "少年时",
                    "Uin": "100028354982"
                },
                "ProductStats": [],
                "RectifyRate": "无需整改",
                "UntreatedRiskCount": 0
            },
            {
                "Member": {
                    "AppId": "1314503630",
                    "MemberId": "mem-1300846651-100027980407",
                    "Nickname": "测试部门",
                    "Uin": "100027980407"
                },
                "ProductStats": [],
                "RectifyRate": "无需整改",
                "UntreatedRiskCount": 0
            }
        ],
        "OverdueAccountCount": 6,
        "OverdueProductCount": 2,
        "RequestId": "6f57db6e-44a6-4d70-9fae-4b9eef649b3b",
        "TotalCount": 6
    }
}
```

