**Example 1: 查询某个收件人列表详情**



Input: 

```
tccli ses ListReceiverDetails --cli-unfold-argument  \
    --ReceiverId 123 \
    --Email abc@ec.cm \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Email": "abc@cd.com",
                "CreateTime": "2021-09-28 16:40:35",
                "TemplateData": "{\"name\":\"1\"}"
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

