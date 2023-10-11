**Example 1: 查询用户自定义引擎参数**

查询用户自定义引擎参数

Input: 

```
tccli dlc DescribeUserDataEngineConfig --cli-unfold-argument  \
    --Sorting abc \
    --Limit 0 \
    --Offset 0 \
    --SortBy abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "DataEngineConfigInstanceInfos": [
            {
                "DataEngineId": "abc",
                "DataEngineConfigPairs": [
                    {
                        "ConfigItem": "abc",
                        "ConfigValue": "abc"
                    }
                ],
                "SessionResourceTemplate": {
                    "DriverSize": "abc",
                    "ExecutorSize": "abc",
                    "ExecutorNums": 1,
                    "ExecutorMaxNumbers": 1
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

