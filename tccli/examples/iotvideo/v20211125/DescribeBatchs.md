**Example 1: 获取批次列表**



Input: 

```
tccli iotvideo DescribeBatchs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ProductId 37MFSSRMZY
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Status": 1,
                "DevNum": 1,
                "UpdateTime": 1612237826,
                "DevNumCreated": 1,
                "DevPre": "test",
                "UserId": "100004557990",
                "CreateTime": 1612237826,
                "BatchURL": "url",
                "Id": 1,
                "ProductId": "37MFSSRMZY"
            }
        ],
        "RequestId": "719fe65a"
    }
}
```

