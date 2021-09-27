**Example 1: 查询应用列表**



Input: 

```
tccli cwp DescribeAssetAppList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Apps": [
            {
                "OsInfo": "xx",
                "Version": "xx",
                "MachineWanIp": "xx",
                "Uuid": "xx",
                "ProjectId": 1,
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
                "ProcessCount": 1,
                "Desc": "xx",
                "Type": 1,
                "MachineIp": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

