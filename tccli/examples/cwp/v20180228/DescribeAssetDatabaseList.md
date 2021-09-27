**Example 1: 查询资产管理数据库列表**



Input: 

```
tccli cwp DescribeAssetDatabaseList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "xx",
        "Databases": [
            {
                "OsInfo": "xx",
                "Version": "xx",
                "MachineWanIp": "xx",
                "ErrorLogPath": "xx",
                "Proto": "xx",
                "ProjectId": 1,
                "Permission": "xx",
                "LogPath": "xx",
                "DataPath": "xx",
                "Param": "xx",
                "ConfigPath": "xx",
                "BinPath": "xx",
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "Quuid": "xx",
                "PlugInPath": "xx",
                "Ip": "xx",
                "Uuid": "xx",
                "Name": "xx",
                "Port": "xx",
                "MachineIp": "xx",
                "User": "xx"
            }
        ]
    }
}
```

