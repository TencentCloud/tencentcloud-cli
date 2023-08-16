**Example 1: 批量操作任务列表**

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
            "PageCount": 1,
            "Items": [
                {
                    "TaskId": "abc",
                    "TaskName": "abc",
                    "WorkflowId": "abc",
                    "WorkflowName": "abc",
                    "Status": "abc",
                    "TaskTypeId": 1,
                    "TaskTypeDesc": "abc",
                    "FolderName": "abc",
                    "FolderId": "abc",
                    "InCharge": "abc",
                    "Submit": 1,
                    "DataEngine": "abc",
                    "UpdateTime": "abc",
                    "CreateTime": "abc",
                    "CycleUnit": "abc",
                    "ScheduleDesc": "abc"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 查询失败**

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

