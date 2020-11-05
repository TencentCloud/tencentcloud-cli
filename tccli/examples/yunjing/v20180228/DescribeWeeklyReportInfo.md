**Example 1: Getting details in weekly CWP Pro report**

This example shows you how to get the details in the weekly CWP Pro report.

Input: 

```
tccli yunjing DescribeWeeklyReportInfo --cli-unfold-argument  \
    --BeginDate 2018-10-08
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "CompanyName": "Component name",
        "MachineNum": 100,
        "OnlineMachineNum": 80,
        "OfflineMachineNum": 20,
        "ProVersionMachineNum": 30,
        "MalwareNum": 11,
        "NonlocalLoginNum": 11,
        "BruteAttackSuccessNum": 11,
        "VulNum": 11,
        "DownloadUrl": "http://download-url.com/xxx.xlsx",
        "Level": "LOW",
        "BeginDate": "2018-10-08",
        "EndDate": "2018-10-13"
    }
}
```

