**Example 1: 获取AI模型版本**



Input: 

```
tccli tcr ListAIModelVersions --cli-unfold-argument  \
    --RegistryId tcr-kpf**etb \
    --NamespaceName ml-skills \
    --RepositoryName skill-translate
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "VersionList": [
            {
                "IsRecommended": false,
                "PushTime": "2026-03-23T13:27:14.977Z",
                "Size": 134813,
                "Version": "v2.0.0"
            }
        ],
        "RequestId": "7323a77d-6e33-40c5-b737-ce2d3ebcd250"
    }
}
```

