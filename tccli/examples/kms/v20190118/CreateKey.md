**Example 1: 创建主密钥示例**

创建用户管理数据密钥的主密钥CMK（Custom Master Key），通过CMK后续可以调用其他接口诸如创建数据密钥、加解密等操作。

Input: 

```
tccli kms CreateKey --cli-unfold-argument  \
    --Alias mykey \
    --KeyUsage ENCRYPT_DECRYPT \
    --Description test
```

Output: 
```
{
    "Response": {
        "KeyId": "9999aed0-4956-11e9-bc70-5254005e86b4",
        "Alias": "alias-0001",
        "CreateTime": 1552897190,
        "Description": "test cmk",
        "TagMsg": "Success",
        "TagCode": 0,
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "RequestId": "850bf779-2249-4995-8c55-b3966daf0a8c",
        "HsmClusterId": ""
    }
}
```

