**Example 1: CreateSession示例**



Input: 

```
tccli gs CreateSession --cli-unfold-argument  \
    --UserId 字符串型 \
    --GameId 字符串型 \
    --GameRegion 字符串型 \
    --ClientSession 字符串型
```

Output: 
```
{
    "Response": {
        "RoleNumber": "xx",
        "ServerSession": "xx",
        "Role": "xx",
        "RequestId": "xx",
        "PlayersMax": 1
    }
}
```

