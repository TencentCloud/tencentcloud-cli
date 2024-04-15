**Example 1: 查询失败**

查询失败

Input: 

```
tccli wedata DescribeBatchOperateTask --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --TaskNameFilter  \
    --TaskIdFilter  \
    --OwnerNameFilter  \
    --Page 1 \
    --Size 20 \
    --SortItem  \
    --SortType 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "Connect to 9.164.239.24:54220 [/9.164.239.24] failed: Connection refused (Connection refused) executing POST http://data-source/cloud/datasource/v1/DescribeDataSourceWithoutInfo"
        },
        "RequestId": "2be30f31-ec77-4f92-abd1-0f5b9113fb0e"
    }
}
```

**Example 2: 批量操作任务列表**

批量操作任务列表

Input: 

```
tccli wedata DescribeBatchOperateTask --cli-unfold-argument  \
    --ProjectId 1464951627049713664 \
    --TaskNameFilter  \
    --TaskIdFilter  \
    --OwnerNameFilter  \
    --Page 1 \
    --Size 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2023-03-21 19:39:28",
                    "CycleUnit": "D",
                    "DataEngine": null,
                    "DatasourceId": null,
                    "DatasourceType": null,
                    "FolderId": "29c8c4f2-7953-11ed-8346-e43d1ad5f5f0",
                    "FolderName": "jayshi",
                    "InCharge": ";zheyuwang;",
                    "ScheduleDesc": "每天00:00执行一次",
                    "Status": "Y",
                    "Submit": 0,
                    "TaskId": "20230321193928764",
                    "TaskName": "20230321",
                    "TaskTypeDesc": "Shell",
                    "TaskTypeId": 35,
                    "UpdateTime": "2024-03-14 14:28:09",
                    "WorkflowId": "0302ca9b-c7dd-11ed-8346-e43d1ad5f5f0",
                    "WorkflowName": "dataflow_20230321"
                }
            ],
            "PageCount": 70,
            "TotalCount": 700
        },
        "RequestId": "df914542-61ca-4c16-80d3-c2a9211425c7"
    }
}
```

