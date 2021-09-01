**Example 1: 获取某代理商的解绑客户列表**



Input: 

```
tccli partners DescribeUnbindClientList --cli-unfold-argument  \
    --Status 1 \
    --UnbindUin xx \
    --ApplyTimeEnd 2020-09-22 \
    --Limit 1 \
    --Offset 1 \
    --ApplyTimeStart 2020-09-22
```

Output: 
```
{
    "Response": {
        "RequestId": "78b52639-8471-41c1-a05a-1ea787a605e0",
        "TotalCount": 1,
        "UnbindClientList": [
            {
                "Uin": 12345678,
                "Name": "xxx",
                "Status": 1,
                "ApplyTime": "2020-09-22 00:00:00",
                "ActionTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

