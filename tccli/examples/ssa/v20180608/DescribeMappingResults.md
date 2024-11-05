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
                    "AssetType": "cvm",
                    "AssetCount": 1
                }
            ],
            "Result": [
                {
                    "AssetName": "name",
                    "AssetIp": "132.*.*.*",
                    "PrivateIp": "10.0.0.1",
                    "AssetId": "1",
                    "Protocol": "http",
                    "Port": "443",
                    "Service": "nginx",
                    "Component": "nginx",
                    "Process": "nginx",
                    "OS": "centos7",
                    "LastMappingTime": "2020-10-10 12:12:12",
                    "DisposalRecommendations": "need to dispose",
                    "DisposalRecommendationDetails": "need to dispose",
                    "AssetType": "cvm",
                    "Domain": "excample.com",
                    "MappingStatus": 1,
                    "Region": "ap-guangzhou",
                    "SecurityStatus": [
                        {
                            "Type": "1",
                            "Status": 1
                        }
                    ],
                    "DisposalRecommendation": 0,
                    "MappingType": "1"
                }
            ],
            "TaskCount": 1,
            "TaskMaxCount": 1
        },
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead"
    }
}
```

