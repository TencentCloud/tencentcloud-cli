**Example 1: 查询资产管理内核模块列表**



Input: 

```
tccli cwp DescribeAssetCoreModuleList --cli-unfold-argument  \
    --Uuid xx \
    --Order asc \
    --Limit 1 \
    --Quuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --By xx
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Modules": [
            {
                "OsInfo": "xx",
                "Name": "xx",
                "MachineName": "xx",
                "Id": "xx",
                "Version": "xx",
                "ModuleCount": 1,
                "ProcessCount": 1,
                "Path": "xx",
                "Size": 1,
                "MachineIp": "xx",
                "Desc": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

