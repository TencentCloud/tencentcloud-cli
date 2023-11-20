**Example 1: 查询只读组中只读部分的默认权重**



Input: 

```
tccli sqlserver DescribeReadOnlyGroupAutoWeight --cli-unfold-argument  \
    --InstanceId mssql-2cwisu23 \
    --ReadOnlyGroupId mssqlrg-itaunotj
```

Output: 
```
{
    "Response": {
        "IsOfflineDelay": 1,
        "MasterInstanceId": "mssql-2cwisu23",
        "MinReadOnlyInGroup": 2,
        "ReadOnlyGroupId": "mssqlrg-itaunotj",
        "ReadOnlyGroupName": "",
        "ReadOnlyInstanceSet": [
            {
                "AccountDifference": "",
                "Cpu": 1,
                "CreateTime": "2019-12-20 10:11:37",
                "DatabaseDifference": "",
                "DelayTime": "",
                "EndTime": "",
                "InstanceId": "mssqlro-otx9r1gr",
                "IsolateTime": "",
                "Memory": 2,
                "Model": 2,
                "Name": "66c5d5b3-bf78-4f3c-b4e5-047d8d6aad49",
                "PayMode": 1,
                "ProjectId": 0,
                "StartTime": "",
                "Status": 2,
                "Storage": 20,
                "SynStatus": "",
                "Type": "TS85",
                "Uid": "",
                "UpdateTime": "2021-10-20 17:31:48",
                "Version": "2008R2",
                "Weight": 1
            }
        ],
        "ReadOnlyMaxDelayTime": 3,
        "RegionId": "",
        "RequestId": "1055ece1-7c6d-4442-aa20-1e8b588f8444",
        "Status": 5,
        "SubnetId": "",
        "Vip": "10.0.0.198",
        "VpcId": "",
        "Vport": 1433,
        "ZoneId": ""
    }
}
```

