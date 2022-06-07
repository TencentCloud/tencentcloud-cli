**Example 1: 模型列表请求**



Input: 

```
tccli tione DescribeTrainingModels --cli-unfold-argument  \
    --Filters.0.Fuzzy True \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.Negative True \
    --TagFilters.0.TagValues xx \
    --TagFilters.0.TagKey xx \
    --Limit 0 \
    --OrderField xx \
    --Offset 0 \
    --Order xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "TrainingModels": [
            {
                "TrainingModelName": "xx",
                "TrainingModelId": "xx",
                "CreateTime": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            }
        ]
    }
}
```

