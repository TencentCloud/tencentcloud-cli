**Example 1: CreateSession示例**

锁定实例后，创建会话，以连接实例

Input: 

```
tccli gs CreateSession --cli-unfold-argument  \
    --GameRegion 字符串型 \
    --GameId 字符串型 \
    --UserId 字符串型 \
    --ClientSession 字符串型
```

Output: 
```
{
    "Response": {
        "RoleNumber": "1",
        "ServerSession": "abc",
        "Role": "Player",
        "RequestId": "req123"
    }
}
```

