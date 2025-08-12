**Example 1: 创建投递dlc任务**



Input: 

```
tccli cls CreateDlcDeliver --cli-unfold-argument  \
    --TopicId 6bf3355c-3c88-4566-89c8-76c3ca37bae9 \
    --Name test1 \
    --DeliverType 0 \
    --StartTime 1741005340 \
    --DlcInfo.TableInfo.DataDirectory /a/a/a/a \
    --DlcInfo.TableInfo.DatabaseName database_name \
    --DlcInfo.TableInfo.TableName table_name \
    --DlcInfo.FieldInfos.0.ClsField cls_1 \
    --DlcInfo.FieldInfos.0.DlcField dlc_1 \
    --DlcInfo.FieldInfos.0.DlcFieldType string \
    --DlcInfo.FieldInfos.1.ClsField dlc_2 \
    --DlcInfo.FieldInfos.1.DlcField dlc_2 \
    --DlcInfo.FieldInfos.1.DlcFieldType int \
    --DlcInfo.FieldInfos.1.Disable True \
    --DlcInfo.PartitionInfos.0.ClsField cls_1 \
    --DlcInfo.PartitionInfos.0.DlcField dlc_1 \
    --DlcInfo.PartitionInfos.0.DlcFieldType string \
    --MaxSize 5 \
    --Interval 300 \
    --HasServicesLog 2
```

Output: 
```
{
    "Response": {
        "RequestId": "09e2ab6b-97fe-47eb-917c-bfb1e6c218e0",
        "TaskId": "23428151-15cc-48ce-a2de-d02e186ddcf8"
    }
}
```

