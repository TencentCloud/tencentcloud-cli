**Example 1: 获取特征洞察统计**

通过Type=1获取特征洞察统计

Input: 

```
tccli apcas QueryGeneralStat --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "GeneralStat": {
            "TodayAmount": 122222,
            "WeekAmount": 2222,
            "MonthAmount": 299333,
            "TotalAmount": 10000
        }
    }
}
```

