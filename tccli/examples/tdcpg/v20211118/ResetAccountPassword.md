**Example 1: 重置数据库账号密码**



Input: 

```
tccli tdcpg ResetAccountPassword --cli-unfold-argument  \
    --ClusterId tdcpg-xxx \
    --AccountName account \
    --AccountPassword 1234@abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

