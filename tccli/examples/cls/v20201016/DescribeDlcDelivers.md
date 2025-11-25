**Example 1: 获取日志主题下的dlc投递任务**



Input: 

```
tccli cls DescribeDlcDelivers --cli-unfold-argument  \
    --TopicId 6bf3355c-3c88-4566-89c8-76c3ca37bae9 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "BizType": 0,
                "CreateTime": 1742466273,
                "DeliverType": 0,
                "DlcInfo": {
                    "FieldInfos": [
                        {
                            "ClsField": "cls_1",
                            "DlcField": "dlc_1",
                            "DlcFieldType": "string"
                        },
                        {
                            "ClsField": "dlc_2",
                            "Disable": true,
                            "DlcField": "dlc_2",
                            "DlcFieldType": "int"
                        }
                    ],
                    "PartitionInfos": [
                        {
                            "ClsField": "cls_1",
                            "DlcField": "dlc_1",
                            "DlcFieldType": "string"
                        }
                    ],
                    "TableInfo": {
                        "DataDirectory": "/a/a/a/a",
                        "DatabaseName": "database_name",
                        "TableName": "table_name"
                    }
                },
                "HasServicesLog": 2,
                "Interval": 300,
                "MaxSize": 5,
                "Name": "test10",
                "StartTime": 1741005340,
                "Status": 1,
                "TaskId": "b0266f31-3224-4a6d-856c-01ba021939b9",
                "TopicId": "6bf3355c-3c88-4566-89c8-76c3ca37bae9",
                "Uin": 100001127589,
                "UpdateTime": 1742466273
            }
        ],
        "RequestId": "4162c1e2-abaf-457e-b25c-4ba5b6a13bd8",
        "Total": 10
    }
}
```

