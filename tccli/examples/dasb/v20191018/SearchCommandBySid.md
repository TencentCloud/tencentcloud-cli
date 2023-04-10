**Example 1: 根据会话Id搜索Command**

根据会话Id搜索Command

Input: 

```
tccli dasb SearchCommandBySid --cli-unfold-argument  \
    --Sid xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "CommandSet": [
            {
                "TimeOffset": 1,
                "Action": 0,
                "Cmd": "xx",
                "Time": "xx"
            }
        ]
    }
}
```

