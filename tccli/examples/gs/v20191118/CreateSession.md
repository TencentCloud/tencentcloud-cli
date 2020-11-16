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
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022",
        "RoleNumber": "Player0",
        "ServerSession": "xyz"
    }
}
```

