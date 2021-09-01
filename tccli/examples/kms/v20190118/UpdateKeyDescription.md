**Example 1: 修改主密钥描述信息示例**

对指定的CMK修改描述信息

Input: 

```
tccli kms UpdateKeyDescription --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --Description NewDescription
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

