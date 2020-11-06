**Example 1: 批量启用主密钥示例**

对指定的CMK 列表进行批量启用。

Input: 

```
tccli kms EnableKeys --cli-unfold-argument  \
    --KeyIds 23e80852-1e38-11e9-b129-5cb9019b4b01 23e80852-1e38-11e9-b129-5cb9019b4b02
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

