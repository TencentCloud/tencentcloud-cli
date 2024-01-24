**Example 1: 查询用户数据开发浏览历史**



Input: 

```
tccli wedata DescribeBrowsingHistories --cli-unfold-argument  \
    --ProjectId abc \
    --TopN 0 \
    --ResourceType abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Title": "abc",
                "VisitTime": "2020-09-22T00:00:00+00:00",
                "ExtraInfo": "abc",
                "ResourceType": "abc",
                "ResourceId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

