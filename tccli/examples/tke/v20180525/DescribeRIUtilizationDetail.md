**Example 1: Filter Name值不支持**

Filter Name只支持文档中的示例值

Input: 

```
tccli tke DescribeRIUtilizationDetail --cli-unfold-argument  \
    --Filters.0.Name not-support-filter-name
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Filter Name:not-support-filter-name not supported"
        },
        "RequestId": "e6a4cb0c-defc-4829-8c12-784f300cea6a"
    }
}
```

**Example 2: DescribeRIUtilizationDetail**



Input: 

```
tccli tke DescribeRIUtilizationDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RIUtilizationDetailSet": [],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

**Example 3: 查询时间范围内的抵扣记录**

查询时间范围内的抵扣记录

Input: 

```
tccli tke DescribeRIUtilizationDetail --cli-unfold-argument  \
    --Filters.0.Name begin-time \
    --Filters.0.Values '2023-08-09 00:00:00' \
    --Filters.1.Name end-time \
    --Filters.1.Values '2023-08-09 01:00:00'
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RIUtilizationDetailSet": [],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

