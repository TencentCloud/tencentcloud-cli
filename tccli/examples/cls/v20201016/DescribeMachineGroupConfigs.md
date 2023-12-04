**Example 1: 获取机器组绑定的采集规则配置**

获取机器组绑定的采集规则配置

Input: 

```
tccli cls DescribeMachineGroupConfigs --cli-unfold-argument  \
    --GroupId 01fd5bcc-d7d4-4edb-9ff5-7ecfc305b831
```

Output: 
```
{
    "Response": {
        "Configs": [
            {
                "AdvancedConfig": "",
                "ConfigId": "16c904ed-db2a-4ba4-b6fd-0f5f94f71111",
                "CreateTime": "2023-06-28 15:58:16",
                "ExcludePaths": null,
                "ExtractRule": {
                    "Address": "",
                    "Backtracking": -1,
                    "BeginRegex": "",
                    "Delimiter": "",
                    "EventLogRules": [],
                    "FilterKeyRegex": [],
                    "IsGBK": 0,
                    "JsonStandard": 0,
                    "Keys": null,
                    "LogRegex": "",
                    "MetaTags": [],
                    "MetadataType": 0,
                    "ParseProtocol": "",
                    "PathRegex": "",
                    "Protocol": "",
                    "TimeFormat": "",
                    "TimeKey": "",
                    "UnMatchLogKey": "LogParseFailure",
                    "UnMatchUpLoadSwitch": false
                },
                "LogFormat": "",
                "LogType": "json_log",
                "Name": "cls_hkff7p5e_test_c_eks",
                "Output": "a004adec-c87a-4179-b0eb-8f7ee4ec1111",
                "Path": "/var/log/eks-log-agent/test-c/*/*/**/*.log",
                "UpdateTime": "2023-11-16 21:42:48",
                "UserDefineRule": ""
            }
        ],
        "RequestId": "983cd59e-7a7a-48aa-a16f-b0f0275c2288"
    }
}
```

