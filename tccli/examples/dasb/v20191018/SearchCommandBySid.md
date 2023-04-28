**Example 1: 根据会话Id搜索Command**

根据会话Id搜索Command

Input: 

```
tccli dasb SearchCommandBySid --cli-unfold-argument  \
    --Sid 123
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "abc123",
        "CommandSet": [
            {
                "TimeOffset": 1,
                "Action": 0,
                "Cmd": "rm",
                "Time": "2023-04-23T14:24:39+0800"
            }
        ]
    }
}
```

