**Example 1: 云台控制**

成功响应

Input: 

```
tccli weilingwith ControlCameraPTZ --cli-unfold-argument  \
    --WID c6cb1e55-7bd7-4f08-a97b-0b530f8a66f3 \
    --CMD left \
    --WorkspaceId 1016 \
    --ApplicationToken ct5E8QNPQEZZqNW7ShPAJQVzrTV9xIbL
```

Output: 
```
{
    "Response": {
        "RequestId": "745845ec-f5be-4e2f-87b6-8e46b9269d0a",
        "Result": {
            "Msg": "ok"
        }
    }
}
```

