**Example 1: 创建作业定义**



Input: 

```
tccli dlc CreateJobDefinition --cli-unfold-argument  \
    --Name spark-demo \
    --MinorType SPARK_SQL \
    --RunMode WAREHOUSE \
    --WarehouseId wh-8f21c3
```

Output: 
```
{
    "Response": {
        "JobDefinitionId": "jd-4b7e15",
        "RequestId": "f4a1c9b2-7d3e-4a58-9c62-1e8b5d7a2f43"
    }
}
```

