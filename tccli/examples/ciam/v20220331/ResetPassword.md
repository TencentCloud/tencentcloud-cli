**Example 1: 重置用户密码**



Input: 

```
tccli ciam ResetPassword --cli-unfold-argument  \
    --UserId 53e25c3****************e4eb5bd1 \
    --UserStoreId 2c3aca3b****************a7efe88e
```

Output: 
```
{
    "Response": {
        "Password": "password",
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

