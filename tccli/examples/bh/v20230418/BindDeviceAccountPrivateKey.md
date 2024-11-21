**Example 1: 绑定主机账号私钥**

绑定主机账号私钥

Input: 

```
tccli bh BindDeviceAccountPrivateKey --cli-unfold-argument  \
    --PrivateKey bh-test-key \
    --Id 1 \
    --PrivateKeyPassword bh-test-key-pwd
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

