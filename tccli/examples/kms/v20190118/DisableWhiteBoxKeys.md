**Example 1: 批量禁用白盒密钥**



Input: 

```
tccli kms DisableWhiteBoxKeys --cli-unfold-argument  \
    --KeyIds 23e80852-1e38-11e9-b129-5cb9019b4b02 23e80852-1e38-11e9-b129-5cb9019b4b01
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

