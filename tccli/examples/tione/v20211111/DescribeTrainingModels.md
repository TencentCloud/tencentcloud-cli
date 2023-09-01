**Example 1: 模型列表请求**

模型列表请求

Input: 

```
tccli tione DescribeTrainingModels --cli-unfold-argument  \
    --Filters.0.Fuzzy False \
    --Filters.0.Values NORMAL \
    --Filters.0.Name ModelVersionType \
    --Filters.0.Negative False \
    --TagFilters.0.TagValues test-value \
    --TagFilters.0.TagKey test-key \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TrainingModels": [
            {
                "TrainingModelId": "m-660879334503305216",
                "TrainingModelName": "test-model",
                "Tags": [
                    {
                        "TagKey": "test-key",
                        "TagValue": "test-value"
                    }
                ],
                "CreateTime": "2022-11-17 20:09:16",
                "TrainingModelVersions": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659"
    }
}
```

