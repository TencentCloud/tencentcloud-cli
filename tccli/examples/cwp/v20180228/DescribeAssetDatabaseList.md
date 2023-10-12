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
                "MachineIp": "abc",
                "MachineWanIp": "abc",
                "Quuid": "abc",
                "Uuid": "abc",
                "OsInfo": "abc",
                "ProjectId": 1,
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "abc",
                        "TagId": 1
                    }
                ],
                "Name": "abc",
                "Version": "abc",
                "Port": "abc",
                "Proto": "abc",
                "User": "abc",
                "Ip": "abc",
                "ConfigPath": "abc",
                "LogPath": "abc",
                "DataPath": "abc",
                "Permission": "abc",
                "ErrorLogPath": "abc",
                "PlugInPath": "abc",
                "BinPath": "abc",
                "Param": "abc",
                "Id": "abc",
                "UpdateTime": "abc",
                "FirstTime": "abc",
                "IsNew": 0,
                "MachineName": "abc",
                "MachineExtraInfo": {
                    "WanIP": "abc",
                    "PrivateIP": "abc",
                    "NetworkType": 0,
                    "NetworkName": "abc",
                    "InstanceID": "abc",
                    "HostName": "abc"
                }
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

