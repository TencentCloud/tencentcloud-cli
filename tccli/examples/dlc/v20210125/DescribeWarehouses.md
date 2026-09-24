**Example 1: 查询计算仓库列表**



Input: 

```
tccli dlc DescribeWarehouses --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --Filters.0.Name State \
    --Filters.0.Operator EQ \
    --Filters.0.Values RUNNING \
    --SortFields.0.Field WarehouseId \
    --SortFields.0.Order ASC
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WarehouseList": [
            {
                "WarehouseId": "wh-8f21c3",
                "Name": "spark-demo",
                "CreatorSubUin": "700281534962",
                "Description": "演示用途的配置",
                "State": "RUNNING",
                "PartitionCode": "dlc-p-nwruuglc",
                "PartitionName": "spark-demo-partition",
                "QueueName": "root.default",
                "CreateTime": 1767256876123,
                "UpdateTime": 1767256876123,
                "ActiveClusters": 1,
                "MinClusters": 1,
                "MaxClusters": 4,
                "RuntimeCode": "spark-3.5.5",
                "RuntimeName": "Spark 3.5.5",
                "SysCatalogVersion": "TCCATALOG",
                "EnvVars": [
                    {
                        "Key": "spark.executor.memory",
                        "Value": "4g"
                    }
                ],
                "RuntimeConf": "{\"spark.driver.cores\":\"1\"}",
                "DynamicProperties": "{\"spark.executor.instances\":\"2\"}"
            }
        ],
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

