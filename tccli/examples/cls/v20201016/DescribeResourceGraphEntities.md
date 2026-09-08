**Example 1: 分页查询资源列表**



Input: 

```
tccli cls DescribeResourceGraphEntities --cli-unfold-argument  \
    --ResourceGraphId test-yunapi-full \
    --NextCursor db2a083497*******b***********40f \
    --Limit 3 \
    --FromTime 1782230000 \
    --ToTime 1782231000
```

Output: 
```
{
    "Response": {
        "NextCursor": "002b693f4f8cd075e2c6a750e6e58e2c",
        "RequestId": "93445bae-45f7-4d5c-bdc4-1a7f5d8a753f"
    }
}
```

**Example 2: 带过滤条件查询**



Input: 

```
tccli cls DescribeResourceGraphEntities --cli-unfold-argument  \
    --ResourceGraphId badc7d81-70a6-4979-aa54-59ae51a4870a \
    --Filters.0.Key Product \
    --Filters.0.Values tke
```

Output: 
```
{
    "Response": {
        "NextCursor": "",
        "RequestId": "32666ac9-87d7-49ab-aa01-98c569817625"
    }
}
```

**Example 3: 查询资源图谱列表**



Input: 

```
tccli cls DescribeResourceGraphEntities --cli-unfold-argument  \
    --ResourceGraphId test-yunapi-full \
    --Limit 3 \
    --FromTime 1782230000 \
    --ToTime 1782231000
```

Output: 
```
{
    "Response": {
        "NextCursor": "001fee59f00b6253231a932c4a8200b3",
        "RequestId": "59515df4-b220-44bf-ab0d-019df54edf21"
    }
}
```

