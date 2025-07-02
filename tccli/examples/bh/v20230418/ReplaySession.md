**Example 1: 会话回放**

会话回放

Input: 

```
tccli bh ReplaySession --cli-unfold-argument  \
    --Sid d6021542-c198-4d6f-a1fd-a8091544847c
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082",
        "ReplayInfo": {
            "Token": "eyJhbGciOiJFUzUx",
            "StartTime": "2025-07-01T19:25:31+08:00",
            "Address": "wss://bh.cloud.tencent.com/tui/replay",
            "ReplayType": 0
        }
    }
}
```

