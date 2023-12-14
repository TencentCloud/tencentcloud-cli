**Example 1: 获取设备列表详情**

获取租户满足条件：最近登录账号包含\'cc\'（不区分大小写）的设备列表详情

Input: 

```
tccli ioa DescribeDevices --cli-unfold-argument  \
    --Condition.FilterGroups.0.Filters.0.Field IOAUserName \
    --Condition.FilterGroups.0.Filters.0.Operator ilike \
    --Condition.FilterGroups.0.Filters.0.Values cc \
    --Condition.PageSize 10 \
    --Condition.PageNum 1 \
    --GroupId 93 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Paging": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 2
            }
        },
        "RequestId": "807938c5-9308-4c87-918d-e84a05f226a1"
    }
}
```

