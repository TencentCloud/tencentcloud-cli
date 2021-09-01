**Example 1: 导入密钥对**



Input: 

```
tccli lighthouse ImportKeyPair --cli-unfold-argument  \
    --KeyName test_import \
    --PublicKey <公钥内容>
```

Output: 
```
{
    "Response": {
        "KeyId": "lhkp-2xsmy15f",
        "RequestId": "87e6cf6c-1734-497e-aed5-9e12afa7237a"
    }
}
```

