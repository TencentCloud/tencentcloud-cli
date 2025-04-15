**Example 1: 查询用户自定义引擎参数**

查询用户自定义引擎参数

Input: 

```
tccli dlc DescribeUserDataEngineConfig --cli-unfold-argument  \
    --Sorting asc \
    --Limit 10 \
    --Offset 0 \
    --SortBy create-time \
    --Filters.0.Name engine-id \
    --Filters.0.Values DataEngine-engineid
```

Output: 
```
{
    "Response": {
        "DataEngineConfigInstanceInfos": [
            {
                "DataEngineConfigPairs": [
                    {
                        "ConfigItem": "spark.dlc.extensions.scope",
                        "ConfigValue": "functions"
                    },
                    {
                        "ConfigItem": "spark.sql.extensions",
                        "ConfigValue": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions, org.apache.kyuubi.plugin.spark.authz.ranger.RangerSparkExtension,org.apache.spark.dlc.extensions.DLCSparkSessionExtensions"
                    }
                ],
                "DataEngineId": "DataEngine-engineid",
                "SessionResourceTemplate": {
                    "DriverSize": "large",
                    "ExecutorMaxNumbers": 3,
                    "ExecutorNums": 3,
                    "ExecutorSize": "large"
                }
            }
        ],
        "RequestId": "3735e957-b4c3-49f3-abce-7a2f21e80e9d",
        "TotalCount": 1
    }
}
```

