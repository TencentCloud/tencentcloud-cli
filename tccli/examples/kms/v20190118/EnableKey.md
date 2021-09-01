**Example 1: 启用主密钥示例**

启用一个主密钥，允许该 CMK 被使用。

Input: 

```
tccli kms EnableKey --cli-unfold-argument  \
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

