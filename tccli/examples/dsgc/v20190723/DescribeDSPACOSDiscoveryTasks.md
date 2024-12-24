**Example 1: 获取COS分类分级任务列表**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTasks --cli-unfold-argument  \
    --DspaId dspa-12cd45g7 \
    --TaskId 0 \
    --Name apple \
    --StatusList 0 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Name": "cos分类分级任务",
                "Description": "cos分类分级任务",
                "Period": 0,
                "Plan": 0,
                "Enable": 1,
                "DataSourceInfo": {
                    "ResourceRegion": "ap-guangzhou",
                    "DataSourceId": "cos-d653b75c5bac583e5003012eff6cf40ecbadfe3c",
                    "DataSourceName": "kyrie-cos-test-251007922",
                    "ProxyAddress": [],
                    "Condition": {
                        "Bucket": "kyrie-cos-test-251007922",
                        "FileTypes": [
                            ".txt"
                        ],
                        "FileSizeLimit": 102400
                    }
                },
                "GeneralRuleSetEnable": 0,
                "TimingStartTime": "2024-11-07 22:40:19",
                "ComplianceUpdate": true,
                "Result": {
                    "Id": 1,
                    "EndTime": "2024-11-07 22:41:19",
                    "Status": 4,
                    "Result": "ComplianceConfigError"
                }
            }
        ],
        "RequestId": "0f3bffa9-2993-0df7-0301-4a8c9fe74aa7",
        "TotalCount": 0
    }
}
```

