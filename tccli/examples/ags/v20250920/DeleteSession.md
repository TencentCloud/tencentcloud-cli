**Example 1: 删除会话**

删除指定会话空间下的指定会话。

Input: 

```
tccli ags DeleteSession --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df \
    --UserId customer-32874915 \
    --SessionId session-order-assistance-20260817-0001
```

Output: 
```
{
    "Response": {
        "RequestId": "afdb8139-1c10-475b-876d-6b8d791a8a2e"
    }
}
```

