**Example 1: 查询Jar包列表**



Input: 

```
tccli cwp DescribeAssetJarList --cli-unfold-argument  \
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
        "Jars": [
            {
                "Status": 1,
                "OsInfo": "xx",
                "Name": "xx",
                "MachineName": "xx",
                "Id": "xx",
                "Version": "xx",
                "Path": "xx",
                "Type": 8,
                "MachineIp": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

