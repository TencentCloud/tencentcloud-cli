**Example 1: 创建作业**



Input: 

```
tccli dlc CreateJob --cli-unfold-argument  \
    --JobName spark-sql-demo \
    --MinorType SPARK_SQL \
    --FlowId flow-2a9c4e \
    --ExecutionId exec-6f1b83 \
    --RunMode WAREHOUSE \
    --WarehouseId wh-8f21c3
```

Output: 
```
{
    "Response": {
        "JobId": "job-9f3a2b1c",
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

