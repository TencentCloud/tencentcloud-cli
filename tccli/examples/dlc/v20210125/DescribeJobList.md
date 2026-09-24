**Example 1: 查询作业列表**



Input: 

```
tccli dlc DescribeJobList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --Filters.0.Name MinorType \
    --Filters.0.Operator EQ \
    --Filters.0.Values SPARK_SQL \
    --SortFields.0.Field CreateTime \
    --SortFields.0.Order DESC
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Items": [
            {
                "JobId": "job-9f3a2b1c",
                "JobName": "spark-sql-demo",
                "CreatorSubUin": "700281534962",
                "State": "SUCCEEDED",
                "MajorType": "SPARK",
                "MinorType": "SPARK_SQL",
                "RunMode": "WAREHOUSE",
                "WarehouseId": "wh-8f21c3",
                "PartitionCode": "dlc-p-nwruuglc",
                "PartitionName": "spark-demo-partition",
                "QueueName": "root.default",
                "CheckpointLocation": "cosn://demo-bucket/checkpoints/demo_stream",
                "CreateTime": 1767256876123,
                "SubmitTime": 1767256876123,
                "FinishTime": 1767256876123,
                "RunningTimeMs": 900000,
                "WarehouseName": "spark-warehouse"
            }
        ],
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

