**Example 1: 查询用户组列表**



Input: 

```
tccli clb DescribeUserGroups --cli-unfold-argument  \
    --ModelRouterId cmr-pm53f9c3 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserGroups": [
            {
                "UserGroupId": "ugrp-9f8e7d6c",
                "UserGroupName": "核心业务组",
                "Status": "Active",
                "ModelRouterId": "cmr-pm53f9c3",
                "Models": [
                    "deepseek-v3"
                ],
                "IntentRouters": [
                    "ir-chat"
                ],
                "BudgetId": "budget-x1y2z3",
                "BudgetName": "核心组月度预算",
                "CreditUsageSet": [
                    {
                        "BudgetDuration": "30d",
                        "Limit": 1000.0,
                        "Used": 128.45,
                        "BudgetResetAt": "2026-07-01T00:00:00+08:00"
                    }
                ],
                "KeyCount": 12,
                "Tags": [
                    {
                        "TagKey": "dept",
                        "TagValue": "payments"
                    }
                ],
                "CreatedTime": "2026-06-16T10:00:00Z",
                "ModifiedTime": "2026-06-16T10:00:00Z"
            },
            {
                "UserGroupId": "ugrp-ungrouped",
                "UserGroupName": "ungrouped",
                "Status": "Active",
                "ModelRouterId": "cmr-pm53f9c3",
                "Models": [],
                "IntentRouters": [],
                "BudgetId": "",
                "BudgetName": "",
                "CreditUsageSet": [],
                "KeyCount": 7,
                "Tags": []
            }
        ],
        "RequestId": "d81e7b1f-3587-491b-8556-9e47222fecfd"
    }
}
```

