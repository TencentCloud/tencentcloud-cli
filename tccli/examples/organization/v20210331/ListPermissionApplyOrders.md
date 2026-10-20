**Example 1: 查询管理员审批列表**



Input: 

```
tccli organization ListPermissionApplyOrders --cli-unfold-argument  \
    --ZoneId z-hmdjcgbvm7z2 \
    --SearchValue 1122 \
    --Status 1 \
    --MaxResults 20 \
    --NextToken 
```

Output: 
```
{
    "Response": {
        "ApplyOrders": [],
        "IsTruncated": false,
        "MaxResults": 20,
        "NextToken": "",
        "TotalCounts": 0,
        "RequestId": "42be7cae-eb66-4fde-821b-e28bee186edf"
    }
}
```

