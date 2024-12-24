**Example 1: 示例**

获取dspa实例下的cos资源列表

Input: 

```
tccli dsgc ListDSPACosMetaResources --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --Filters.0.Name Bucket \
    --Filters.0.Values commontest-1252347619 \
    --Offset 1 \
    --Limit 1 \
    --BindType binded
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Items": [
            {
                "Bucket": "commontest-1252347619",
                "CreateTime": "2020-05-07 22:00:00",
                "Valid": 0,
                "ResourceId": "cos-f265c921bb53ed2b24f5593768ad030c5e82220c",
                "ResourceRegion": "ap-guangzhou",
                "BindStatus": "binded",
                "Storage": 3,
                "GovernAuthStatus": 0
            }
        ],
        "DspaId": "dspa-a1b2c3d4",
        "RequestId": "0cf9a026-3679-4205-a676-5449211df926"
    }
}
```

