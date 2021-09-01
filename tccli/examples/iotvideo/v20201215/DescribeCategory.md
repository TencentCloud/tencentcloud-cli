**Example 1: 获取Category详情**



Input: 

```
tccli iotvideo DescribeCategory --cli-unfold-argument  \
    --Id 113
```

Output: 
```
{
    "Response": {
        "Data": {
            "CategoryName": "video",
            "CategoryKey": "video",
            "ListOrder": 1,
            "IconUrl": "url",
            "IconUrlGrid": "grid",
            "ParentId": 0,
            "ModelTemplate": "{}",
            "Id": 113
        },
        "RequestId": "d8de3a44"
    }
}
```

