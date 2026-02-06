**Example 1: 查询实时任务表粒度指标概览**



Input: 

```
tccli wedata DescribeTaskTableMetricOverview --cli-unfold-argument  \
    --TaskId taskId \
    --NodeType NodeType \
    --TaskType 0 \
    --Filters.0.Name Name \
    --Filters.0.Values 1 \
    --PageNumber 0 \
    --PageSize 0 \
    --OrderFields.0.Name Name \
    --OrderFields.0.Direction Direction \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "TaskTableMetricInfos": [
            {
                "DatabaseName": "DatabaseName",
                "TableName": "TableName",
                "TotalRecordNum": 0,
                "TotalRecordByteNum": 0,
                "TotalDirtyRecordNum": 0,
                "SchemaName": "SchemaName",
                "Topic": "Topic",
                "Collection": "Collection",
                "DataSourceName": "DataSourceName",
                "NodeId": "nodeId"
            }
        ],
        "TotalCount": 0,
        "MetricType": "num",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

