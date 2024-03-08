**Example 1: 查询分账报表费用趋势**

查询分账报表费用趋势

Input: 

```
tccli billing DescribeAllocationTrendByMonth --cli-unfold-argument  \
    --Month 2024-02 \
    --TreeNodeUniqKey 合计费用(折后总额)
```

Output: 
```
{
    "Response": {
        "Current": {
            "Month": "2024-02",
            "Name": "2024年02月",
            "RealTotalCost": "32953.81"
        },
        "Previous": [
            {
                "Month": "2023-09",
                "Name": "2023年09月",
                "RealTotalCost": "14372.07"
            },
            {
                "Month": "2023-10",
                "Name": "2023年10月",
                "RealTotalCost": "107337.26"
            },
            {
                "Month": "2023-11",
                "Name": "2023年11月",
                "RealTotalCost": "35828.25"
            },
            {
                "Month": "2023-12",
                "Name": "2023年12月",
                "RealTotalCost": "-1507335.00"
            },
            {
                "Month": "2024-01",
                "Name": "2024年01月",
                "RealTotalCost": "82679.62"
            }
        ],
        "RequestId": "f6f9372f-f7e7-462e-b20a-cbd5b6b77c4d",
        "Stat": {
            "Average": {
                "BeginMonth": "2023-09",
                "EndMonth": "2024-02",
                "RealTotalCost": "-205694.00"
            }
        }
    }
}
```

