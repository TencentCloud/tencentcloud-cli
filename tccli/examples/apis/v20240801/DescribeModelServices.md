**Example 1: 查询模型服务**



Input: 

```
tccli apis DescribeModelServices --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --Offset 0 \
    --Limit 10 \
    --IDs mds-0101 \
    --NotIDs mds-0101 \
    --Status normal \
    --Keyword hehe_tes \
    --ModelID mod-0101 \
    --Sort.CreateTime 1 \
    --Sort.LastUpdateTime 1 \
    --Sort.Name 1 \
    --Sort.Status -1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "Total": 0
        },
        "RequestId": "fedea4c1-a673-4ac2-824c-73a2c9ef5d4f"
    }
}
```

