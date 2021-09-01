**Example 1: 禁用主密钥示例**

禁用指定的CMK。

Input: 

```
tccli kms DisableKey --cli-unfold-argument  \
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

