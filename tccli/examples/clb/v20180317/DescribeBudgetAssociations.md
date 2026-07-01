**Example 1: 查询Budget关联的资源**



Input: 

```
tccli clb DescribeBudgetAssociations --cli-unfold-argument  \
    --BudgetId budget-qygts98h
```

Output: 
```
{
    "Response": {
        "AssociationSet": [
            {
                "BudgetId": "budget-qygts98h",
                "CreatedTime": "2026-04-18T20:31:53+08:00",
                "KeyId": "vkey-gnswk5t5",
                "ModelRouterId": "cmr-3lxl0rmz",
                "Status": "Active",
                "Type": "Key"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d7432208-9ad0-45f5-b004-48863728455b"
    }
}
```

