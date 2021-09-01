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
        "WeeklyReportBruteAttacks": [
            {
                "Username": "xx",
                "SrcIp": "xx",
                "MachineIp": "xx",
                "AttackTime": "2020-09-22 00:00:00",
                "Count": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

