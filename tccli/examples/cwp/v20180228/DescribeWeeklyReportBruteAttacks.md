**Example 1: 获取专业周报密码破解数据**

获取专业周报密码破解数据。

Input: 

```
tccli cwp DescribeWeeklyReportBruteAttacks --cli-unfold-argument  \
    --BeginDate 2018-10-08 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

