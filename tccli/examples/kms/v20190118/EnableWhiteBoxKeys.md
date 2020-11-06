**Example 1: 批量启用白盒密钥**



Input: 

```
tccli kms EnableWhiteBoxKeys --cli-unfold-argument  \
    --KeyIds 23e80852-1e38-11e9-b129-5cb9019b4b01 23e80852-1e38-11e9-b129-5cb9019b4b02
```

Output: 
```
{
    "Response": {
        "RequestId": "850bf779-2249-4995-8c55-b3966daf0a8c"
    }
}
```

