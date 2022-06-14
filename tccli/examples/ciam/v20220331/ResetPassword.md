**Example 1: 重置用户密码**



Input: 

```
tccli ciam ResetPassword --cli-unfold-argument  \
    --UserStoreId xx \
    --UserId xx
```

Output: 
```
{
    "Response": {
        "Password": "xx",
        "RequestId": "xx"
    }
}
```

