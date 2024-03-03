**Example 1: DescribeMappingResults**



Input: 

```
tccli ssa DescribeMappingResults --cli-unfold-argument  \
    --Filter.0.Filter.0.FilterValue ins-3u7e8ki2 \
    --Filter.0.Filter.0.FilterOperatorType 1 \
    --Filter.0.Filter.0.FilterKey AssetId \
    --Filter.0.Logic 1 \
    --PageIndex 1 \
    --PageSize 1 \
    --Sorter.0.SortType 1 \
    --Sorter.0.SortKey LastMappingTime
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": {
            "Statistics": [
                {
                    "AssetType": "abc",
                    "AssetCount": 1
                }
            ],
            "Result": [
                {
                    "AssetName": "abc",
                    "AssetIp": "abc",
                    "PrivateIp": "abc",
                    "AssetId": "abc",
                    "Protocol": "abc",
                    "Port": "abc",
                    "Service": "abc",
                    "Component": "abc",
                    "Process": "abc",
                    "OS": "abc",
                    "LastMappingTime": "abc",
                    "DisposalRecommendations": "abc",
                    "DisposalRecommendationDetails": "abc",
                    "AssetType": "abc",
                    "Domain": "abc",
                    "MappingStatus": 1,
                    "Region": "abc",
                    "SecurityStatus": [
                        {}
                    ],
                    "DisposalRecommendation": 0,
                    "MappingType": "abc"
                }
            ],
            "TaskCount": 1,
            "TaskMaxCount": 1
        },
        "RequestId": "abc"
    }
}
```

