**Example 1: 查询公摊规则概览**



Input: 

```
tccli billing DescribeAllocationRuleSummary --cli-unfold-argument  \
    --Month 2022-11 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "RuleList": [
            {
                "RuleId": 33,
                "RuleName": "测试1",
                "Type": 2,
                "UpdateTime": "2022-10-30 17:26:16",
                "AllocationNode": [
                    {
                        "NodeId": 6,
                        "TreeNodeUniqKeyName": "产品一部"
                    },
                    {
                        "NodeId": 7,
                        "TreeNodeUniqKeyName": "产品二部"
                    },
                    {
                        "NodeId": 8,
                        "TreeNodeUniqKeyName": "产品三部"
                    },
                    {
                        "NodeId": 9,
                        "TreeNodeUniqKeyName": "产品四部"
                    }
                ]
            },
            {
                "RuleId": 29,
                "RuleName": "test_allocation2",
                "Type": 1,
                "UpdateTime": "2022-10-24 12:05:04",
                "AllocationNode": [
                    {
                        "NodeId": 2,
                        "TreeNodeUniqKeyName": "财务部"
                    },
                    {
                        "NodeId": 5,
                        "TreeNodeUniqKeyName": "组织部"
                    }
                ]
            }
        ],
        "RequestId": "78933c15-099c-4958-9ca0-8c148bc1da04"
    }
}
```

