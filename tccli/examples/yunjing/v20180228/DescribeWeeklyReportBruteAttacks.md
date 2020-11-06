**Example 1: 获取专业周报密码破解数据**

获取专业周报密码破解数据。

Input: 

```
tccli yunjing DescribeWeeklyReportBruteAttacks --cli-unfold-argument  \
    --BeginDate 2018-10-08 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "WeeklyReportMalwares": [
            {
                "MachineIp": "10.10.10.12",
                "Username": "root",
                "SrcIp": "139.12.12.12",
                "AttackTime": "2018-10-11 12:12:22",
                "Count": 10
            }
        ],
        "TotalCount": 100
    }
}
```

