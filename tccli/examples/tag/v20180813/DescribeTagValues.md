**Example 1: 查询标签值**



Input: 

```
tccli tag DescribeTagValues --cli-unfold-argument  \
    --TagKeys test1
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
                "TagKey": "test1",
                "TagValue": "test"
            }
        ],
        "RequestId": "69e59dbe-71e4-4497-a735-abdd7bf5f50a"
    }
}
```

