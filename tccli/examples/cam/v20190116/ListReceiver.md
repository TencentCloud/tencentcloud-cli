**Example 1: 获取消息接收人列表**



Input: 

```
tccli cam ListReceiver --cli-unfold-argument  \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Receivers": [
            {
                "Uid": 1001892,
                "Name": "nick",
                "Remark": "",
                "PhoneNumber": "+86 186****3509",
                "PhoneFlag": 1,
                "Email": "2054****@qq.com",
                "EmailFlag": 1,
                "IsReceiverOwner": 1
            }
        ],
        "RequestId": "9a9d4601-5f14-4293-b314-2319ab9f5450"
    }
}
```

