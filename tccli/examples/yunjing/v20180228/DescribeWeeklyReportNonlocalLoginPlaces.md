**Example 1: Getting unusual login location data in weekly CWP Pro report**

This example shows you how to get the unusual login location data in the weekly CWP Pro report.

Input: 

```
tccli yunjing DescribeWeeklyReportNonlocalLoginPlaces --cli-unfold-argument  \
    --BeginDate 2018-10-08\
    --Limit 10\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "WeeklyReportNonlocalLoginPlaces": [
            {
                "MachineIp": "10.10.10.12",
                "Username": "root",
                "SrcIp": "139.12.12.12",
                "Country": 1,
                "Province": 1,
                "City": 1,
                "LoginTime": "2018-10-11 12:12:22"
            }
        ],
        "TotalCount": 100
    }
}
```

