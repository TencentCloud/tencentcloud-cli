**Example 1: 查询模型列表**



Input: 

```
tccli apis DescribeModels --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --Offset 0 \
    --Limit 10 \
    --IDs 010101 \
    --NotIDs 0202020 \
    --CredentialID 0303030 \
    --Keyword hehe \
    --Sort.CreateTime 1 \
    --Sort.LastUpdateTime 1 \
    --Sort.Name -1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "Total": 0
        },
        "RequestId": "dc855e1e-41fd-4a12-9c19-4fdab33e96e3"
    }
}
```

