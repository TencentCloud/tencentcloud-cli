**Example 1: 获取数据加工任务基本信息**

获取数据加工任务基本信息

Input: 

```
tccli cls DescribeDataTransformInfo --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "DataTransformTaskInfos": [
            {
                "BackupGiveUpData": false,
                "BackupTopicID": "7557cd30-xxxx-xxxx-93d4-7-1254077820",
                "CreateTime": "2024-11-29 03:46:57",
                "DataTransformType": 0,
                "DstResources": [
                    {
                        "Alias": "apilog",
                        "TopicId": "7f670b29-xxxx-xxxx-a62a-dd026fe66a9f"
                    }
                ],
                "EnableFlag": 1,
                "EtlContent": "log_keep(op_or(op_str_eq(v(\"logtype\"), \"apilog\"), op_str_eq(v(\"logtype\"), \"ailog\"), op_str_eq(v(\"logtype\"), \"stlog\"), op_str_eq(v(\"logtype\"), \"ranklog\")))\next_json(\"request\")\next_json(\"messages\")\next_json(\"response\")\next_json(\"completion\")",
                "FailureLogKey": "ETLParseFailure",
                "HasServicesLog": 2,
                "KeepFailureLog": 1,
                "LastEnableTime": "2024-11-29 14:43:18",
                "LogsetId": "6718ed86-xxxx-xxxx-95e1-24012ee15caf",
                "Name": "提取 ClsAi Text2CQL API 访问日志",
                "SrcTopicId": "0bb6b5e6-xxxx-469a-xxxx-ebbe250d083c",
                "SrcTopicName": "[Test] Text2CQL - 全量日志",
                "Status": 2,
                "TaskDstCount": 1,
                "TaskId": "5d368d4c-xxxx-xxxx-87a6-39802c1e0afe",
                "Type": 1,
                "UpdateTime": "2024-11-29 14:45:01"
            }
        ],
        "RequestId": "bf128f9e-xxxx-xxxx-a591-185220479620",
        "TotalCount": 30
    }
}
```

