**Example 1: 获取cos导入配置**

获取cos导入配置

Input: 

```
tccli cls DescribeCosRecharges --cli-unfold-argument  \
    --TopicId fadcc986-xxxx-xxxx-b766-9ce9c193da32 \
    --Status 0 \
    --Enable 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "9b3cc796-xxxx-xxxx-90e0-e760f1d991a0",
                "TopicId": "fadcc986-xxxx-xxxx-b766-9ce9c193da32",
                "LogsetId": "bcc26ed4-xxxx-xxxx-9992-cea8ff7cf470",
                "Name": "cos_test1",
                "Bucket": "bucket-1254000000",
                "BucketRegion": "ap-guangzhou",
                "Prefix": "",
                "LogType": "json_log",
                "Status": 2,
                "Enable": 0,
                "Progress": 0,
                "CreateTime": "2024-04-23 15:41:07",
                "UpdateTime": "2024-12-30 20:39:41",
                "Compress": "",
                "ExtractRuleInfo": {
                    "TimeKey": "",
                    "TimeFormat": "",
                    "Delimiter": "",
                    "LogRegex": "",
                    "BeginRegex": "",
                    "Keys": [],
                    "FilterKeyRegex": [],
                    "UnMatchUpLoadSwitch": true,
                    "UnMatchLogKey": "LogParseFailure",
                    "Backtracking": null,
                    "IsGBK": 0,
                    "JsonStandard": 1,
                    "Protocol": "",
                    "Address": "",
                    "ParseProtocol": "",
                    "MetadataType": 0,
                    "PathRegex": "",
                    "MetaTags": [],
                    "EventLogRules": [],
                    "AdvanceFilterRules": [
                        {
                            "Key": "response_code",
                            "Rule": 0,
                            "Value": "400|500"
                        }
                    ]
                },
                "TaskType": 1,
                "Metadata": []
            }
        ],
        "RequestId": "c54d737b-xxxx-xxxx-b3da-c226a6aebaf4"
    }
}
```

