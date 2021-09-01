**Example 1: 查询广州二区的高可用版本售卖规格**



Input: 

```
tccli sqlserver DescribeProductConfig --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --InstanceType HA
```

Output: 
```
{
    "Response": {
        "RequestId": "2a91dd2e-f237-4c78-b06c-348a12b04a46",
        "SpecInfoList": [
            {
                "CPU": 16,
                "InstanceType": "HA",
                "MachineType": "TS85",
                "MachineTypeName": "高IO",
                "MaxStorage": 3000,
                "Memory": 128,
                "MinStorage": 10,
                "MultiZonesStatus": "ALL",
                "PayModeStatus": "ALL",
                "Pid": 10908,
                "PostPid": [
                    10908
                ],
                "QPS": 61000,
                "SpecId": 22,
                "SuitInfo": "独立用户数上千万人的大型应用",
                "Version": "2008R2",
                "VersionName": "SQL Server 2008 Enterprise"
            },
            {
                "CPU": 1,
                "InstanceType": "HA",
                "MachineType": "TS85",
                "MachineTypeName": "高IO",
                "MaxStorage": 3000,
                "Memory": 8,
                "MinStorage": 10,
                "MultiZonesStatus": "ALL",
                "PayModeStatus": "ALL",
                "Pid": 10908,
                "PostPid": [
                    10908
                ],
                "QPS": 6500,
                "SpecId": 17,
                "SuitInfo": "独立用户数上千人的小型应用",
                "Version": "2012SP3",
                "VersionName": "SQL Server 2012 Enterprise"
            },
            {
                "CPU": 24,
                "InstanceType": "HA",
                "MachineType": "TS85",
                "MachineTypeName": "高IO",
                "MaxStorage": 3000,
                "Memory": 192,
                "MinStorage": 10,
                "MultiZonesStatus": "ALL",
                "PayModeStatus": "ALL",
                "Pid": 10908,
                "PostPid": [
                    10908
                ],
                "QPS": 234000,
                "SpecId": 34,
                "SuitInfo": "独立用户数上亿人的大型应用",
                "Version": "2012SP3",
                "VersionName": "SQL Server 2012 Enterprise"
            },
            {
                "CPU": 16,
                "InstanceType": "HA",
                "MachineType": "TS85",
                "MachineTypeName": "高IO",
                "MaxStorage": 3000,
                "Memory": 128,
                "MinStorage": 10,
                "MultiZonesStatus": "ALL",
                "PayModeStatus": "ALL",
                "Pid": 10908,
                "PostPid": [
                    10908
                ],
                "QPS": 61000,
                "SpecId": 22,
                "SuitInfo": "独立用户数上千万人的大型应用",
                "Version": "2016SP1",
                "VersionName": "SQL Server 2016 Enterprise"
            }
        ],
        "TotalCount": 4
    }
}
```

