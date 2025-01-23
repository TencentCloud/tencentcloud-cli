**Example 1: 查询收件人列表**



Input: 

```
tccli ses ListReceivers --cli-unfold-argument  \
    --Status 1 \
    --Offset 1 \
    --Limit 1 \
    --KeyWord keyword
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Count": 1,
                "ReceiversStatus": 1,
                "ReceiverId": 123,
                "ReceiversName": "name",
                "CreateTime": "2021-09-28 16:40:35",
                "Desc": "some description"
            }
        ],
        "RequestId": "38049379278d43208c59916a4806b0c4"
    }
}
```

