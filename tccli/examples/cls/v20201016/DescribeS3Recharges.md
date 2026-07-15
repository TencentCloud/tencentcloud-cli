**Example 1: 查询s3导入任务列表**



Input: 

```
tccli cls DescribeS3Recharges --cli-unfold-argument  \
    --TopicId 3faf22cb-5396-4aca-a3c3-c0831917aa15 \
    --Filters.0.Key bucket \
    --Filters.0.Values echo*************597 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "AccessKeyId": "AKI**************CQG",
                "Bucket": "echo*************597",
                "Compress": "gzip",
                "CreateTime": 1783153774,
                "Enable": 1,
                "Endpoint": "https://cos.example.com",
                "ExtractRule": {
                    "Address": "",
                    "AdvanceFilterRules": [],
                    "Backtracking": null,
                    "BeginRegex": "\\[\\d+-\\d+-\\w+:\\d+:\\d+,\\d+\\]\\s+\\[\\w+\\]\\s+.*",
                    "Delimiter": "",
                    "EventLogRules": [],
                    "FilterKeyRegex": [],
                    "IsGBK": 0,
                    "JsonStandard": 0,
                    "Keys": [
                        "timestamp"
                    ],
                    "LogRegex": "\\s*\\[(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2},\\d{3})\\]\\s+\\[(\\w+)\\]\\s+([\\s\\S]*)\\s*",
                    "MetaTags": [],
                    "MetadataType": 0,
                    "ParseProtocol": "",
                    "PathRegex": "",
                    "Protocol": "",
                    "RawLogKey": "",
                    "TimeFormat": "",
                    "TimeKey": "",
                    "UnMatchLogKey": "LogParseFailure",
                    "UnMatchUpLoadSwitch": true
                },
                "LogType": "multiline_fullregex_log",
                "LogsetId": "7fb0245e-2006-4e0f-9153-c5f6b7110b4c",
                "Metadata": [
                    "bucket"
                ],
                "Name": "test_del_1",
                "Prefix": "csv/",
                "Progress": 0,
                "S3Region": "ap-so*********",
                "Status": 0,
                "TaskId": "b2fbb75a-b5ee-479c-9db4-541c63c0b4c4",
                "TaskType": 1,
                "TopicId": "3faf22cb-5396-4aca-a3c3-c0831917aa15",
                "UpdateTime": 1783153774
            }
        ],
        "Total": 2,
        "RequestId": "ce50cc05-e9ea-49cf-88f5-3d5aa2346986"
    }
}
```

