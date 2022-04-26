**Example 1: 查询资源标签列表**



Input: 

```
tccli tag GetResources --cli-unfold-argument  \
    --ResourceList qcs::cvm:ap-beijing:uin/100000558920:instance/ins-123 qcs::cvm:ap-shanghai:uin/100000558920:instance/ins-345 \
    --TagFilters.0.TagKey 11 \
    --TagFilters.0.TagValue 11 \
    --TagFilters.1.TagKey 22 \
    --TagFilters.1.TagValue 22
```

Output: 
```
{
    "Response": {
        "PaginationToken": "",
        "ResourceTagMappingList": [
            {
                "Resource": "qcs::cvm:ap-beijing:uin/100000558920:instance/ins-123",
                "Tags": [
                    {
                        "TagKey": "22",
                        "TagValue": "22"
                    },
                    {
                        "TagKey": "11",
                        "TagValue": "11"
                    }
                ]
            },
            {
                "Resource": "qcs::cvm:ap-shanghai:uin/100000558920:instance/ins-345",
                "Tags": [
                    {
                        "TagKey": "22",
                        "TagValue": "22"
                    },
                    {
                        "TagKey": "11",
                        "TagValue": "11"
                    }
                ]
            }
        ],
        "RequestId": "07cfd251-4ed1-426c-8133-e04a583063c0"
    }
}
```

