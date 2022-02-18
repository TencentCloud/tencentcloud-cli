**Example 1: 创建收件人列表**



Input: 

```
tccli ses CreateReceiver --cli-unfold-argument  \
    --ReceiversName 收件人列表名称 \
    --Desc 列表描述
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "ReceiverId": 123
    }
}
```

