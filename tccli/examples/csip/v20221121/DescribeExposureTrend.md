**Example 1: 查询互联网暴露周期数量趋势统计信息**

展示互联网暴露数量周期变化

Input: 

```
tccli csip DescribeExposureTrend --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ExposeIncrement": 6,
        "AclCount": 26,
        "CloseCount": 8,
        "OpenCount": 89,
        "ExposeTrendList": [
            {
                "AclCount": 26,
                "CloseCount": 8,
                "Date": "2025-01-15",
                "OpenCount": 89
            }
        ],
        "RequestId": "a98cde8a-3870-433e-bd8f-a491f4981cd2"
    }
}
```

