**Example 1: 获取专业版周报漏洞数据**

获取专业版周报漏洞数据

Input: 

```
tccli yunjing DescribeWeeklyReportVuls --cli-unfold-argument  \
    --BeginDate 2018-10-08
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "WeeklyReportVuls": [
            {
                "MachineIp": "10.10.10.12",
                "VulName": "漏洞名称",
                "Description": "漏洞描述",
                "VulType": "WEB",
                "VulStatus": "FIXED",
                "LastScanTime": "2018-10-11 12:23:22"
            }
        ],
        "TotalCount": 100
    }
}
```

