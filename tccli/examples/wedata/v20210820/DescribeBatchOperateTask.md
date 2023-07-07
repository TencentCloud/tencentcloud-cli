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
        "RequestId": "111",
        "Data": {
            "PageCount": 2,
            "Items": [
                {
                    "TaskId": "20230511100454288",
                    "TaskName": "test_0511",
                    "WorkflowId": "e1812347-cb9d-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "test_0326",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "peanutzhu",
                    "FolderId": "6460a2a0-a36c-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";peanutzhu;",
                    "Submit": 0,
                    "DataEngine": "SparkJob",
                    "UpdateTime": "2023-05-11 13:32:17",
                    "CreateTime": "2023-05-11 10:04:54"
                },
                {
                    "TaskId": "20230508122336184",
                    "TaskName": "123",
                    "WorkflowId": "fbfd3751-960f-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "quinnzhu_wf",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "quinnzhu",
                    "FolderId": "ef5312e0-960f-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";quinnzhu;",
                    "Submit": 0,
                    "DataEngine": "SparkSql",
                    "UpdateTime": "2023-05-08 12:23:53",
                    "CreateTime": "2023-05-08 12:23:36"
                },
                {
                    "TaskId": "20230506181308005",
                    "TaskName": "dlc_sparkbatch_20230506",
                    "WorkflowId": "8684b2a1-ebf6-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "jayshi_dataflow_import_20230506",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "jayshi",
                    "FolderId": "85528199-7a00-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";jayshi;",
                    "Submit": 0,
                    "DataEngine": "SparkSql",
                    "UpdateTime": "2023-05-06 18:42:16",
                    "CreateTime": "2023-05-06 18:13:08"
                },
                {
                    "TaskId": "20230214103702595",
                    "TaskName": "dlc_sql001",
                    "WorkflowId": "5e06de60-ac10-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "hui",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "默认文件夹",
                    "FolderId": "8f6701ca-7618-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";hhhuilli;",
                    "Submit": 0,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-03-01 16:12:10",
                    "CreateTime": "2023-02-14 10:37:02"
                },
                {
                    "TaskId": "20230301101409737",
                    "TaskName": "test_dlc_sql_1",
                    "WorkflowId": "abab662f-b7d6-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "test_workflow_0301",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "charlesccao",
                    "FolderId": "a094275e-b7d6-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";charlesccao;",
                    "Submit": 0,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-03-01 10:14:28",
                    "CreateTime": "2023-03-01 10:14:09"
                },
                {
                    "TaskId": "20230228104842424",
                    "TaskName": "test_ds",
                    "WorkflowId": "611b57d0-b712-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "ds",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "xt",
                    "FolderId": "5a9f9f8e-b712-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";liuxuetong;",
                    "Submit": 0,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-02-28 16:58:54",
                    "CreateTime": "2023-02-28 10:48:42"
                },
                {
                    "TaskId": "20230219221346528",
                    "TaskName": "dlc_sql_20230219",
                    "WorkflowId": "115a42b7-ab2d-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "jayshi_20230213_dlc_secret",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "jayshi",
                    "FolderId": "85528199-7a00-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";jayshi;",
                    "Submit": 0,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-02-19 22:14:04",
                    "CreateTime": "2023-02-19 22:13:46"
                },
                {
                    "TaskId": "20230213210629465",
                    "TaskName": "dlcsql_2023021301",
                    "WorkflowId": "115a42b7-ab2d-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "jayshi_20230213_dlc_secret",
                    "Status": "NL",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "jayshi",
                    "FolderId": "85528199-7a00-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";jayshi;",
                    "Submit": 1,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-02-13 21:06:47",
                    "CreateTime": "2023-02-13 21:06:29"
                },
                {
                    "TaskId": "20230210194032828",
                    "TaskName": "test_dlc_tmp_token",
                    "WorkflowId": "ac60857e-a937-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "test_dlc_tmp_token",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "kaiqidong",
                    "FolderId": "9d7f5165-a937-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";kaiqidong;",
                    "Submit": 0,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-02-13 10:15:07",
                    "CreateTime": "2023-02-10 19:40:32"
                },
                {
                    "TaskId": "20230111105542926",
                    "TaskName": "dlc_02",
                    "WorkflowId": "6b02e62f-7a87-11ed-a3a7-b8cef6c14251",
                    "WorkflowName": "wf_vmscript",
                    "Status": "NS",
                    "TaskTypeId": 32,
                    "TaskTypeDesc": "DLC SQL",
                    "FolderName": "zhanglin",
                    "FolderId": "5c1fd2b9-7a87-11ed-a3a7-b8cef6c14251",
                    "InCharge": ";zhanglin;zheyuwang;",
                    "Submit": 0,
                    "DataEngine": "presto",
                    "UpdateTime": "2023-02-13 09:45:43",
                    "CreateTime": "2023-01-11 10:55:42"
                }
            ]
        }
    }
}
```

