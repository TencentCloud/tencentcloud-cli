**Example 1: 查询资产管理环境变量列表**



Input: 

```
tccli cwp DescribeAssetEnvList --cli-unfold-argument  \
    --Uuid xx \
    --Limit 1 \
    --Quuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Envs": [
            {
                "OsInfo": "xx",
                "Name": "xx",
                "MachineName": "xx",
                "Value": "xx",
                "User": "xx",
                "Type": 1,
                "MachineIp": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

