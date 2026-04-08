**Example 1: 请求一个正在处理中的话术**



Input: 

```
tccli live DescribeLiveAvatarScripts --cli-unfold-argument  \
    --RoomId 1002
```

Output: 
```
{
    "Response": {
        "InfoList": [
            {
                "Title": "title",
                "Content": "hello",
                "CreateTime": "2025-07-02T07:19:08Z",
                "ProductId": "1002",
                "ScriptId": "100",
                "Duration": 0,
                "Status": "PENDING",
                "UpdateTime": "2025-07-02T07:19:08Z"
            }
        ],
        "LimitCreateNum": 100,
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "TotalNum": 1
    }
}
```

