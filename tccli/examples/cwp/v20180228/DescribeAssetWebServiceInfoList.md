**Example 1: 查询资产管理Web服务列表**



Input: 

```
tccli cwp DescribeAssetWebServiceInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WebServices": [
            {
                "OsInfo": "xx",
                "Version": "xx",
                "Quuid": "xx",
                "MachineWanIp": "xx",
                "Uuid": "xx",
                "InstallPath": "xx",
                "ProjectId": 1,
                "ConfigPath": "xx",
                "Id": "xx",
                "BinPath": "xx",
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "User": "xx",
                "ProcessCount": 1,
                "MachineIp": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

