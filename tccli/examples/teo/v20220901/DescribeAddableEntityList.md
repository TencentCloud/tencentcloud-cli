**Example 1: 查询剩余可添加的四层代理列表**



Input: 

```
tccli teo DescribeAddableEntityList --cli-unfold-argument  \
    --EntityType domain \
    --ZoneId zone-28v4ag8bprrm \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EntityList": [
            "sub.example.com"
        ],
        "RequestId": "8fbf8770-6bc2-48e1-a544-bf06eb8481e6"
    }
}
```

