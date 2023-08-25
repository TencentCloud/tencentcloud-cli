**Example 1: 示例**

获取dspa实例下的cos资源列表

Input: 

```
tccli dsgc ListDSPACosMetaResources --cli-unfold-argument  \
    --DspaId abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 1 \
    --Limit 1 \
    --BindType abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Items": [
            {
                "Bucket": "abc",
                "CreateTime": "abc",
                "Valid": 0,
                "ResourceId": "abc",
                "ResourceRegion": "abc",
                "BindStatus": "abc",
                "Storage": 1
            }
        ],
        "DspaId": "abc",
        "RequestId": "abc"
    }
}
```

