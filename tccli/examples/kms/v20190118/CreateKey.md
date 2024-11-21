**Example 1: 创建主密钥示例**

创建用户管理数据密钥的主密钥CMK（Custom Master Key），通过CMK后续可以调用其他接口诸如创建数据密钥、加解密等操作。

Input: 

```
tccli kms CreateKey --cli-unfold-argument  \
    --Description test描述 \
    --Alias test8-lzc \
    --KeyUsage ENCRYPT_DECRYPT \
    --Type 1 \
    --Tags.0.TagKey env \
    --Tags.0.TagValue dev
```

Output: 
```
{
    "Response": {
        "Alias": "test8-lzc",
        "CreateTime": 1730347170,
        "Description": "test描述",
        "HsmClusterId": "cls-hsm-3dflmo9g",
        "KeyId": "87ff856e-973c-11ef-947b-525400d834e5",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "RequestId": "c44aba41-015a-45aa-9e55-1a08ac9d1d78",
        "TagCode": 0,
        "TagMsg": "ok"
    }
}
```

