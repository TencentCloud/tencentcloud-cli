**Example 1: 查询服务进程信息**

查询服务进程信息

Input: 

```
tccli emr DescribeServiceNodeInfos --cli-unfold-argument  \
    --InstanceId emr-3u \
    --Limit 999 \
    --Offset 0 \
    --ServiceName HIVE
```

Output: 
```
{
    "Response": {
        "AliasInfo": "13141313",
        "RequestId": "a90a9922-dc51-45a6-abdd-93f63cf02e57",
        "ServiceNodeList": [
            {
                "ConfGroupId": 623383,
                "ConfGroupName": "hive-master-defaultGroup",
                "ConfStatus": 1,
                "DataNodeMaintenanceState": 0,
                "Flag": 1,
                "HAState": "",
                "HealthStatus": {
                    "Code": 1,
                    "Desc": "端口探测在5s内响应",
                    "Text": "良好"
                },
                "Ip": "10.0.0.0",
                "IsFederation": false,
                "IsSupportRoleMonitor": true,
                "LastRestartTime": "2024-08-16 14:13:32",
                "MonitorStatus": 1,
                "NameService": "",
                "NodeFlagFilter": "master",
                "NodeName": "HiveMetaStore",
                "NodeType": 30,
                "PortsInfo": "",
                "ServiceDetectionInfo": [],
                "ServiceStatus": 1,
                "Status": 1,
                "StopPolicies": null
            },
            {
                "ConfGroupId": 623383,
                "ConfGroupName": "hive-master-defaultGroup",
                "ConfStatus": 1,
                "DataNodeMaintenanceState": 0,
                "Flag": 1,
                "HAState": "",
                "HealthStatus": {
                    "Code": 1,
                    "Desc": "端口探测在5s内响应",
                    "Text": "良好"
                },
                "Ip": "10.0.0.0",
                "IsFederation": false,
                "IsSupportRoleMonitor": true,
                "LastRestartTime": "2024-08-16 14:14:24",
                "MonitorStatus": 1,
                "NameService": "",
                "NodeFlagFilter": "master",
                "NodeName": "HiveMetaStore",
                "NodeType": 30,
                "PortsInfo": "",
                "ServiceDetectionInfo": [],
                "ServiceStatus": 1,
                "Status": 1,
                "StopPolicies": null
            },
            {
                "ConfGroupId": 623383,
                "ConfGroupName": "hive-master-defaultGroup",
                "ConfStatus": 1,
                "DataNodeMaintenanceState": 0,
                "Flag": 1,
                "HAState": "",
                "HealthStatus": {
                    "Code": 1,
                    "Desc": "端口探测在5s内响应",
                    "Text": "良好"
                },
                "Ip": "10.0.0.0",
                "IsFederation": false,
                "IsSupportRoleMonitor": true,
                "LastRestartTime": "2024-08-16 14:14:47",
                "MonitorStatus": 1,
                "NameService": "",
                "NodeFlagFilter": "master",
                "NodeName": "HiveServer2",
                "NodeType": 31,
                "PortsInfo": "",
                "ServiceDetectionInfo": [],
                "ServiceStatus": 1,
                "Status": 1,
                "StopPolicies": null
            },
            {
                "ConfGroupId": 623383,
                "ConfGroupName": "hive-master-defaultGroup",
                "ConfStatus": 1,
                "DataNodeMaintenanceState": 0,
                "Flag": 1,
                "HAState": "",
                "HealthStatus": {
                    "Code": 1,
                    "Desc": "端口探测在5s内响应",
                    "Text": "良好"
                },
                "Ip": "10.0.0.0",
                "IsFederation": false,
                "IsSupportRoleMonitor": true,
                "LastRestartTime": "2024-08-16 14:14:54",
                "MonitorStatus": 1,
                "NameService": "",
                "NodeFlagFilter": "master",
                "NodeName": "HiveServer2",
                "NodeType": 31,
                "PortsInfo": "",
                "ServiceDetectionInfo": [],
                "ServiceStatus": 1,
                "Status": 1,
                "StopPolicies": null
            },
            {
                "ConfGroupId": 623383,
                "ConfGroupName": "hive-master-defaultGroup",
                "ConfStatus": 1,
                "DataNodeMaintenanceState": 0,
                "Flag": 1,
                "HAState": "",
                "HealthStatus": {
                    "Code": 1,
                    "Desc": "端口探测在5s内响应",
                    "Text": "良好"
                },
                "Ip": "10.0.0.0",
                "IsFederation": false,
                "IsSupportRoleMonitor": true,
                "LastRestartTime": "2024-08-16 14:15:11",
                "MonitorStatus": 1,
                "NameService": "",
                "NodeFlagFilter": "master",
                "NodeName": "HiveWebHcat",
                "NodeType": 32,
                "PortsInfo": "",
                "ServiceDetectionInfo": [],
                "ServiceStatus": 1,
                "Status": 1,
                "StopPolicies": null
            },
            {
                "ConfGroupId": 623383,
                "ConfGroupName": "hive-master-defaultGroup",
                "ConfStatus": 1,
                "DataNodeMaintenanceState": 0,
                "Flag": 1,
                "HAState": "",
                "HealthStatus": {
                    "Code": 1,
                    "Desc": "端口探测在5s内响应",
                    "Text": "良好"
                },
                "Ip": "10.0.0.0",
                "IsFederation": false,
                "IsSupportRoleMonitor": true,
                "LastRestartTime": "2024-08-16 14:15:39",
                "MonitorStatus": 1,
                "NameService": "",
                "NodeFlagFilter": "master",
                "NodeName": "HiveWebHcat",
                "NodeType": 32,
                "PortsInfo": "",
                "ServiceDetectionInfo": [],
                "ServiceStatus": 1,
                "Status": 1,
                "StopPolicies": null
            }
        ],
        "SupportNodeFlagFilterList": [
            "master",
            "core",
            "task",
            "common",
            "router"
        ],
        "TotalCnt": 6
    }
}
```

