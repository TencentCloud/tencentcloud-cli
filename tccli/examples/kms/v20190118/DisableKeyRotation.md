**Example 1: 禁止密钥交换示例**

对指定的CMK禁止密钥交换功能。

Input: 

```
tccli kms DisableKeyRotation --cli-unfold-argument  \
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

