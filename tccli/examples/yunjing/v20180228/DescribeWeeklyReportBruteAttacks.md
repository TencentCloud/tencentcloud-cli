**Example 1: Getting brute force attack data in weekly CWP Pro report**

This example shows you how to get the brute force attack data in the weekly CWP Pro report.

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

