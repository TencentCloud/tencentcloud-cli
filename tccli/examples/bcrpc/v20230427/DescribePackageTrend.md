**Example 1: 查询用户套餐用量趋势**



Input: 

```
tccli bcrpc DescribePackageTrend --cli-unfold-argument  \
    --PeriodType 0 \
    --StartTime abc \
    --EndTime abc
```

Output: 
```
{
    "Response": {
        "DataList": [
            {
                "Time": "ac",
                "Value": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

