**Example 1: 获取特殊采集配置**

获取特殊采集配置

Input: 

```
tccli cls DescribeConfigExtras --cli-unfold-argument  \
    --Filters.0.Key configExtraId \
    --Filters.0.Values xxxx-xxx-xxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Configs": [
            {
                "AdvancedConfig": "{\"ClsAgentFileTimeout\":3600}",
                "CollectInfos": [
                    {
                        "CollectConfigs": [
                            {
                                "Name": "container_name"
                            },
                            {
                                "Name": "namespace"
                            },
                            {
                                "Name": "pod_name"
                            },
                            {
                                "Name": "pod_ip"
                            }
                        ],
                        "Type": 0
                    },
                    {
                        "CollectConfigs": [],
                        "Type": 1
                    }
                ],
                "ConfigExtraId": "26ea1681-dfef-4429-a84f-3450d5d46796",
                "ConfigFlag": "label_k8s",
                "ContainerFile": {
                    "Container": "",
                    "CustomLabels": null,
                    "ExcludeLabels": null,
                    "ExcludeNamespace": "",
                    "FilePaths": [],
                    "FilePattern": "",
                    "IncludeLabels": null,
                    "LogPath": "",
                    "Namespace": "",
                    "WorkLoad": {
                        "Container": "",
                        "Kind": "",
                        "Name": "",
                        "Namespace": ""
                    }
                },
                "ContainerStdout": {
                    "AllContainers": true,
                    "Container": "",
                    "CustomLabels": null,
                    "ExcludeLabels": null,
                    "ExcludeNamespace": "",
                    "IncludeLabels": null,
                    "Namespace": "*",
                    "WorkLoads": null
                },
                "CreateTime": "2023-12-04 14:32:35",
                "ExcludePaths": null,
                "ExtractRule": {
                    "Address": "",
                    "Backtracking": 0,
                    "BeginRegex": "",
                    "Delimiter": "",
                    "EventLogRules": [],
                    "FilterKeyRegex": [],
                    "IsGBK": 0,
                    "JsonStandard": 0,
                    "Keys": [
                        "__CONTENT__"
                    ],
                    "LogRegex": "",
                    "MetaTags": [],
                    "MetadataType": 0,
                    "ParseProtocol": "",
                    "PathRegex": "",
                    "Protocol": "",
                    "TimeFormat": "",
                    "TimeKey": "",
                    "UnMatchLogKey": null,
                    "UnMatchUpLoadSwitch": false
                },
                "GroupId": "886bf7a8-7340-4314-8d64-b360da0ffd78",
                "HostFile": {
                    "CustomLabels": null,
                    "FilePattern": "",
                    "LogPath": ""
                },
                "LogFormat": "",
                "LogType": "minimalist_log",
                "LogsetId": "40907915-faa6-46e0-985f-b2fa8c17a080",
                "LogsetName": "logset-test",
                "Name": "config-test-886bf7a8-7340-4314-8d64-b360da0ffd78",
                "TopicId": "b2dcf2e5-9582-4c87-9286-cccccb53889d",
                "TopicName": "topic-test",
                "Type": "container_stdout",
                "UpdateTime": "2023-12-04 14:32:34",
                "UserDefineRule": ""
            }
        ],
        "RequestId": "4e48c681-ebf8-4df1-bf0a-51f689117ac6",
        "TotalCount": 1
    }
}
```

