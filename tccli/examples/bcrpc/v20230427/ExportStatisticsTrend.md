**Example 1: 导出请求统计趋势表单**



Input: 

```
tccli bcrpc ExportStatisticsTrend --cli-unfold-argument  \
    --Type 0 \
    --ApplicationName abc \
    --Chain abc \
    --Network abc \
    --PeriodType 0 \
    --StartTime abc \
    --EndTime abc
```

Output: 
```
{
    "Response": {
        "CosUrl": "abc",
        "RequestId": "ac"
    }
}
```

