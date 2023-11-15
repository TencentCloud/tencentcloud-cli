**Example 1: 批量消警**

成功响应

Input: 

```
tccli weilingwith BatchKillAlarm --cli-unfold-argument  \
    --BeginTime 1693416987 \
    --EndTime 1693417958 \
    --StatusSet processed \
    --WorkspaceId 1016 \
    --UserId 1 \
    --UserName a \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "b834d00c-0a1a-4e86-8765-f7114e905466",
        "Result": {
            "Msg": "ok"
        }
    }
}
```

