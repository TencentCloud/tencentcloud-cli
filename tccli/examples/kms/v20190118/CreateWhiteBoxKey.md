**Example 1: 创建白盒密钥**



Input: 

```
tccli kms CreateWhiteBoxKey --cli-unfold-argument  \
    --Alias test-lzcw2 \
    --Description 白盒测试 \
    --Algorithm SM4
```

Output: 
```
{
    "Response": {
        "DecryptKey": "AACAAAAA0/BswblZOBqsOJY/ST****x9scSvWUFbSG/tGBrMpzuCndKomu/Ig4/G",
        "EncryptKey": "AACAAAAA0/BswblZO****VTtExsaGx9scSvWUFbSG/tGBrMpzuCndKomu/Ig4/G",
        "KeyId": "9fe1e083-9807-11ef-8d67-5254008ae90d",
        "RequestId": "af2946f2-0a41-4d40-9e6e-b6e1e3eb5447",
        "TagCode": 0,
        "TagMsg": "no tags to save"
    }
}
```

