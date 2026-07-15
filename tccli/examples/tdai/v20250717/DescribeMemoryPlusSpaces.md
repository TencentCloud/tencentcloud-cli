**Example 1: 成功查询实例列表**



Input: 

```
tccli tdai DescribeMemoryPlusSpaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreatedAt": "2026-05-14T10:34:01+08:00",
                "CreditUsage": 0,
                "MemoryUsage": 0,
                "Name": "name3",
                "Region": "ap-chengdu",
                "ResourceTags": null,
                "SpaceId": "mem-8z4o2g9v",
                "Status": 1
            }
        ],
        "TotalCount": 3,
        "RequestId": "d08df123-f124-4de3-9587-9ce2f915bdb5"
    }
}
```

