**Example 1: 获取基线忽略策略列表**

获取基线忽略策略列表

Input: 

```
tccli csip DescribeBaselineIgnorePolicyList --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppID": 260083796,
                "AssetType": "HOST",
                "CategoryName": "未授权访问",
                "CreateTime": "2026-09-21T11:24:59Z",
                "ID": 4,
                "ItemID": 4,
                "ItemName": "MongoDB未授权访问",
                "ModifyTime": "2026-09-21T11:25:36Z",
                "Remark": "ignore all",
                "ScopeExcludeList": [
                    "instance-ikk"
                ],
                "ScopeIncludeList": [
                    "instance-tki"
                ],
                "ScopeType": "ALL"
            }
        ],
        "TotalCount": 4,
        "RequestId": "fca4f58d-9419-49c9-a79e-c7f2162ac177"
    }
}
```

