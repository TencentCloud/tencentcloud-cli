**Example 1: 获取资产管理数据库详情**



Input: 

```
tccli cwp DescribeAssetDatabaseInfo --cli-unfold-argument  \
    --Quuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Uuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Id 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82",
        "Database": {
            "OsInfo": "CentOs Bit64",
            "UpdateTime": "2024-10-11 12:23:34",
            "MachineWanIp": "1.1.1.1",
            "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
            "Proto": "tcp",
            "ErrorLogPath": "/root",
            "Ip": "10.0.0.11",
            "Permission": "root",
            "LogPath": "/root",
            "DataPath": "/root",
            "Param": "--config",
            "ConfigPath": "/root",
            "BinPath": "/root",
            "Version": "0.1.1",
            "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
            "PlugInPath": "/root",
            "Name": "test-name",
            "Port": "22",
            "MachineIp": "10.0.0.11",
            "User": "root"
        }
    }
}
```

