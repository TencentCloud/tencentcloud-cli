**Example 1: 自定义登录密钥生成示例**



Input: 

```
tccli tcb CreateCustomLoginKey --cli-unfold-argument  \
    --EnvId abc
```

Output: 
```
{
    "Response": {
        "PrivateKey": "abc",
        "KeyID": "abc",
        "RequestId": "abc"
    }
}
```

