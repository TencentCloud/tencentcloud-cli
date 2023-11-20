**Example 1: 查询全地域售卖规格配置**



Input: 

```
tccli sqlserver DescribeProductSpec --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "eaf9efa1-3d73-45f9-97f5-f0ea26040b93",
        "SpecInfoList": [
            {
                "Info": [
                    {
                        "CPU": 1,
                        "MachineType": "TS85",
                        "MachineTypeName": "高IO",
                        "MaxStorage": 3000,
                        "Memory": 2000000,
                        "MinStorage": 10,
                        "PayModeStatus": "ALL",
                        "Pid": 10908,
                        "PostPid": [
                            10908
                        ],
                        "QPS": 2100,
                        "SpecId": 15,
                        "SuitInfo": "独立用户数上百人的小型应用",
                        "Version": "2008R2",
                        "VersionName": "SQL Server 2008 Enterprise"
                    },
                    {
                        "CPU": 1,
                        "MachineType": "TS85",
                        "MachineTypeName": "高IO",
                        "MaxStorage": 3000,
                        "Memory": 2000000,
                        "MinStorage": 10,
                        "PayModeStatus": "ALL",
                        "Pid": 10908,
                        "PostPid": [
                            10908
                        ],
                        "QPS": 2100,
                        "SpecId": 15,
                        "SuitInfo": "独立用户数上百人的小型应用",
                        "Version": "2012SP3",
                        "VersionName": "SQL Server 2012 Enterprise"
                    },
                    {
                        "CPU": 1,
                        "MachineType": "TS85",
                        "MachineTypeName": "高IO",
                        "MaxStorage": 3000,
                        "Memory": 2000000,
                        "MinStorage": 10,
                        "PayModeStatus": "ALL",
                        "Pid": 10908,
                        "PostPid": [
                            10908
                        ],
                        "QPS": 2100,
                        "SpecId": 15,
                        "SuitInfo": "独立用户数上百人的小型应用",
                        "Version": "2016SP1",
                        "VersionName": "SQL Server 2016 Enterprise"
                    }
                ],
                "RegionId": 1,
                "ZoneId": 100002
            }
        ],
        "TotalCount": 1
    }
}
```

