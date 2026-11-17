**Example 1: 查询互联网暴露周期数量趋势统计信息**

展示互联网暴露数量周期变化

Input: 

```
tccli csip DescribeExposureTrend --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AclCount": 0,
        "CloseCount": 8,
        "ExposeIncrement": 0,
        "ExposeTotalCount": 16,
        "ExposeTrendList": [
            {
                "AclCount": 0,
                "CloseCount": 8,
                "Date": "2026-11-09",
                "OpenCount": 8
            }
        ],
        "OpenCount": 8,
        "ToGovernRiskCount": 13,
        "RequestId": "d3c1bb08-ac40-44e3-8670-a2673874500f"
    }
}
```

