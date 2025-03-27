**Example 1: 查询标签**



Input: 

```
tccli tag DescribeTags --cli-unfold-argument  \
    --TagKey testTagKey \
    --TagValue testTagValue
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Offset": 0,
        "Limit": 15,
        "Tags": [
            {
                "TagKey": "key1",
                "TagValue": "val1",
                "CanDelete": 1
            }
        ],
        "RequestId": "0eebf6af-7ae1-44ec-9cae-3752e8bb911a"
    }
}
```

