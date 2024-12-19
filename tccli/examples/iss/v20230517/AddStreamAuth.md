**Example 1: 成功**

 

Input: 

```
tccli iss AddStreamAuth --cli-unfold-argument  \
    --Id 12345678-abcd-efgh-ijkl-1234567890abcd \
    --PullState 0 \
    --PullSecret a3f9ub8hgj \
    --PullExpired 10 \
    --PushState 0 \
    --PushSecret a3f9ub8hgj \
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
            "PullSecret": "a3f9ub8hgj",
            "PullState": 0,
            "PushExpired": 10,
            "PushSecret": "a3f9ub8hgj",
            "PushState": 0
        },
        "RequestId": "b824ee63-1b76-4d6f-a97b-d26e4c3f4e30"
    }
}
```

