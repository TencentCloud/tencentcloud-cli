**Example 1: 查看cos调用记录文件列表**



Input: 

```
tccli csip DescribeCosIpInvokeRecordFile --cli-unfold-argument  \
    --RelAppId 251002343 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Filters.0.Name CategoryId \
    --Filter.Filters.0.Values 355 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.StartTime 2026-03-13 11:19:17 \
    --Filter.EndTime 2026-03-13 11:55:51
```

Output: 
```
{
    "Response": {
        "Data": [
            "Sensitive_data_data.txt"
        ],
        "DataSet": [
            {
                "CategoryDetails": [
                    {
                        "CategoryId": 355,
                        "CategoryName": "个人敏感信息",
                        "RuleSet": [
                            {
                                "LevelId": 8,
                                "LevelName": "敏感",
                                "LevelScore": 10,
                                "RuleId": 6662,
                                "RuleName": "婚姻状况"
                            }
                        ]
                    }
                ],
                "DirName": "",
                "FileName": "Sensitive_data_data.txt"
            }
        ],
        "Total": 1,
        "RequestId": "bf11ccc9-2a5b-4d9c-9b69-e118192cbf5b"
    }
}
```

