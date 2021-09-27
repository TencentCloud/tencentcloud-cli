**Example 1: 查询资产管理启动服务列表**



Input: 

```
tccli cwp DescribeAssetInitServiceList --cli-unfold-argument  \
    --Uuid xx \
    --Limit 1 \
    --Quuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Services": [
            {
                "Status": 1,
                "OsInfo": "xx",
                "Name": "xx",
                "MachineName": "xx",
                "User": "xx",
                "Path": "xx",
                "Type": 1,
                "MachineIp": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

