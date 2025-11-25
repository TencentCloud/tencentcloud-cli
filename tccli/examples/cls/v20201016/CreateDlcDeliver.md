**Example 1: 创建dlc投递任务**



Input: 

```
tccli cls CreateDlcDeliver --cli-unfold-argument  \
    --TopicId 03334fb8-4d74-4dde-ada6-da4c0d0b2ff8 \
    --Name add_dlc_deliver_test1 \
    --DeliverType 0 \
    --StartTime 1741005340 \
    --DlcInfo.TableInfo.DataDirectory test_table \
    --DlcInfo.TableInfo.DatabaseName test_schema \
    --DlcInfo.TableInfo.TableName test_db \
    --DlcInfo.FieldInfos.0.ClsField cls_test_field1 \
    --DlcInfo.FieldInfos.0.DlcField dlc_test_field1 \
    --DlcInfo.FieldInfos.0.DlcFieldType string \
    --DlcInfo.FieldInfos.0.Disable True \
    --DlcInfo.PartitionInfos.0.ClsField cls_test_field2 \
    --DlcInfo.PartitionInfos.0.DlcField dlc_test_field2 \
    --DlcInfo.PartitionInfos.0.DlcFieldType int \
    --DlcInfo.PartitionExtra.TimeFormat /%Y/%m/%d/%H \
    --DlcInfo.PartitionExtra.TimeZone UTC+08:00 \
    --MaxSize 5 \
    --Interval 300 \
    --EndTime 1741006340 \
    --HasServicesLog 2
```

Output: 
```
{
    "Response": {
        "TaskId": "ba05f9aa-432f-4ccc-9120-b60d1f3a0c20",
        "RequestId": "d2ceec4a-1f59-4508-ae4c-e256c30dea1f"
    }
}
```

