**Example 1: 启用密钥交换示例**

对指定的CMK开启密钥轮换功能。

Input: 

```
tccli kms EnableKeyRotation --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

