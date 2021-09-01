**Example 1: 查询密钥轮换状态**

查询指定的CMK密钥轮换功能是否开启。

Input: 

```
tccli kms GetKeyRotationStatus --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01
```

Output: 
```
{
    "Response": {
        "KeyRotationEnabled": false,
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

