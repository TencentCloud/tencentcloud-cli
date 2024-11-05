**Example 1: 查询资产管理数据库列表**

查询资产管理数据库列表

Input: 

```
tccli cwp DescribeAssetDatabaseList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "MachineIp": "10.0.0.11",
                "MachineWanIp": "1.1.1.1",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "OsInfo": "CentOs Bit64",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "Name": "test-name",
                "Version": "0.1.1",
                "Port": "22",
                "Proto": "tcp",
                "User": "root",
                "Ip": "10.0.0.11",
                "ConfigPath": "/root",
                "LogPath": "/root",
                "DataPath": "/root",
                "Permission": "root",
                "ErrorLogPath": "/root",
                "PlugInPath": "/root",
                "BinPath": "/root",
                "Param": "iparam",
                "Id": "10001",
                "UpdateTime": "2024-10-11 12:23:34",
                "FirstTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "MachineName": "test-name",
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "10.0.0.11",
                    "NetworkType": 0,
                    "NetworkName": "vpc-id",
                    "InstanceID": "ins-id",
                    "HostName": "test-name"
                }
            }
        ],
        "Total": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

