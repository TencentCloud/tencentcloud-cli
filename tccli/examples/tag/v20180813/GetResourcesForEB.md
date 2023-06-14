**Example 1: EB侧查询绑定了标签的资源列表**

EB侧查询绑定了标签的资源列表

Input: 

```
tccli tag GetResourcesForEB --cli-unfold-argument  \
    --TargetUin 1000135******
```

Output: 
```
{
    "Response": {
        "PaginationToken": "8g6eL-RZPznZ******",
        "RequestId": "56989b******",
        "ResourceTagMappingList": [
            {
                "Resource": "qcs::cam::uin/1000135******:role/4611****",
                "Tags": [
                    {
                        "TagKey": "test",
                        "TagValue": "test"
                    }
                ]
            }
        ]
    }
}
```

