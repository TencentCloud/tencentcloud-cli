**Example 1: 获取批次详情**



Input: 

```
tccli iotvideo DescribeBatch --cli-unfold-argument  \
    --BatchId 12
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 1,
            "DevNum": 1,
            "UpdateTime": 1612237826,
            "DevNumCreated": 1,
            "DevPre": "test",
            "UserId": "100004557990",
            "CreateTime": 1612237826,
            "BatchURL": "url",
            "Id": 12,
            "ProductId": "37MFSSRMZY"
        },
        "RequestId": "719fe65a"
    }
}
```

