**Example 1: 获取资产管理数据库详情**



Input: 

```
tccli cwp DescribeAssetDatabaseInfo --cli-unfold-argument  \
    --Quuid xx \
    --Uuid xx \
    --Id xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Database": {
            "OsInfo": "xx",
            "UpdateTime": "xx",
            "MachineWanIp": "xx",
            "Uuid": "xx",
            "Proto": "xx",
            "ErrorLogPath": "xx",
            "Ip": "xx",
            "Permission": "xx",
            "LogPath": "xx",
            "DataPath": "xx",
            "Param": "xx",
            "ConfigPath": "xx",
            "BinPath": "xx",
            "Version": "xx",
            "Quuid": "xx",
            "PlugInPath": "xx",
            "Name": "xx",
            "Port": "xx",
            "MachineIp": "xx",
            "User": "xx"
        }
    }
}
```

