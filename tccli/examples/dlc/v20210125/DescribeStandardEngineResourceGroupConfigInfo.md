**Example 1: 查询标准引擎资源组**

查询标准引擎资源组

Input: 

```
tccli dlc DescribeStandardEngineResourceGroupConfigInfo --cli-unfold-argument  \
    --Filters.0.Name engine-id \
    --Filters.0.Values DataEngine-81iy0oxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "90bcc66d-c102-4441-8987-7cc77a733f55",
        "StandardEngineResourceGroupConfigInfos": [
            {
                "CreateTime": 1715136398,
                "DataEngineId": "DataEngine-81iy0oxxx",
                "DynamicConfigPairs": [],
                "ResourceGroupId": "rg-fu11wgexxx",
                "StaticConfigPairs": [],
                "UpdateTime": 1715136398
            }
        ],
        "Total": 1
    }
}
```

