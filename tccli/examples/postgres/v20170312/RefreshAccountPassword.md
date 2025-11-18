**Example 1: 刷新启用CAM验证的账户密码**



Input: 

```
tccli postgres RefreshAccountPassword --cli-unfold-argument  \
    --DBInstanceId postgres-r95q23pn \
    --UserName root
```

Output: 
```
{
    "Response": {
        "RequestId": "1ed5066a-cfad-47e4-b4db-9681166db6e5"
    }
}
```

