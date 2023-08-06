**Example 1: 成功**

 

Input: 

```
tccli iss AddStreamAuth --cli-unfold-argument  \
    --Id 12345678-abcd-efgh-ijkl-1234567890abcd \
    --PullState 0 \
    --PullSecret 123456 \
    --PullExpired 10 \
    --PushState 0 \
    --PushSecret 123456 \
    --PushExpired 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": 1300000000,
            "Id": "12345678-abcd-efgh-ijkl-1234567890abcd",
            "PullExpired": 10,
            "PullSecret": "123456",
            "PullState": 0,
            "PushExpired": 10,
            "PushSecret": "123456",
            "PushState": 0
        },
        "RequestId": "b824ee63-1b76-4d6f-a97b-d26e4c3f4e30"
    }
}
```

