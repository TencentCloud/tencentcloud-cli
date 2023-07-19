**Example 1: 获取采集配置**

根据主题ID获取采集配置详情

Input: 

```
tccli cls DescribeConfigs --cli-unfold-argument  \
    --Filters.0.Key topicId \
    --Filters.0.Values 97e8a872-xxxx-4644-9d3c-603d95051458 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Configs": [
            {
                "ConfigId": "02f11930-xxxx-4dca-8c9b-b6a147223945",
                "Name": "test",
                "LogFormat": "",
                "Path": "/test/**/test",
                "LogType": "minimalist_log",
                "ExtractRule": {
                    "TimeKey": "",
                    "TimeFormat": "",
                    "Delimiter": "",
                    "LogRegex": "",
                    "BeginRegex": "",
                    "Keys": null,
                    "FilterKeyRegex": [],
                    "UnMatchUpLoadSwitch": false,
                    "UnMatchLogKey": null,
                    "Backtracking": 0,
                    "IsGBK": 0,
                    "JsonStandard": 0,
                    "Protocol": "",
                    "Address": "",
                    "ParseProtocol": "",
                    "MetadataType": 0,
                    "PathRegex": "",
                    "MetaTags": []
                },
                "ExcludePaths": null,
                "Output": "97e8a872-xxxx-4644-9d3c-603d95051458",
                "UpdateTime": "2022-09-02 14:26:49",
                "CreateTime": "2022-09-02 14:26:49",
                "UserDefineRule": ""
            }
        ],
        "TotalCount": 2,
        "RequestId": "6eff3561-xxxx-4502-b625-3eb26c4ab450"
    }
}
```

