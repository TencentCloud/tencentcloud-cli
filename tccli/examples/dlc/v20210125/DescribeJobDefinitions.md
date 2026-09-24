**Example 1: 查询作业定义列表**



Input: 

```
tccli dlc DescribeJobDefinitions --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --Filters.0.Name MinorType \
    --Filters.0.Operator EQ \
    --Filters.0.Values SPARK_SQL \
    --SortFields.0.Field UpdateTime \
    --SortFields.0.Order DESC
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Items": [
            {
                "JobDefinitionId": "jd-4b7e15",
                "Name": "spark-demo",
                "Description": "演示用途的配置",
                "MajorType": "SPARK",
                "MinorType": "SPARK_SQL",
                "CheckpointLocation": "cosn://demo-bucket/checkpoints/demo_stream",
                "CreatorSubUin": "700281534962",
                "CreateTime": 1767256876123,
                "UpdateTime": 1767256876123,
                "PartitionCode": "dlc-p-nwruuglc",
                "PartitionName": "spark-demo-partition",
                "QueueName": "root.default",
                "RunMode": "WAREHOUSE",
                "WarehouseId": "wh-8f21c3",
                "InstanceCount": 1,
                "RuntimeCode": "spark-3.5.5",
                "RuntimeName": "Spark 3.5.5",
                "WarehouseName": "spark-warehouse"
            }
        ],
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

