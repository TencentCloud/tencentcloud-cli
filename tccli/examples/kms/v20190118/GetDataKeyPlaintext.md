**Example 1: 获取数据密钥明文示例**

获取数据密钥明文

Input: 

```
tccli kms GetDataKeyPlaintext --cli-unfold-argument  \
    --DataKeyId cb0f16e6-4f49-11f0-b672-52540073b995
```

Output: 
```
{
    "Response": {
        "Plaintext": "3434",
        "RequestId": "bd05b0b7-8019-44cf-a67e-fd9a940cee82"
    }
}
```

