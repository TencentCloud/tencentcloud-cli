**Example 1: 获取指定任务产出登记列表**



Input: 

```
tccli wedata DescribeTaskOutputRegistries --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "TaskName": "abc",
                "ProjectId": "abc",
                "DatasourceId": "abc",
                "DatabaseName": "abc",
                "TableName": "abc",
                "PartitionName": "abc",
                "Id": 12,
                "DataFlowType": "abc",
                "CreateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

