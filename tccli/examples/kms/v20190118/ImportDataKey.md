**Example 1: 数据密钥导入示例**



Input: 

```
tccli kms ImportDataKey --cli-unfold-argument  \
    --DataKeyName test_weijia_0123456 \
    --ImportKeyMaterial MTIzNAo= \
    --ImportType 2 \
    --Description 数据密钥导入测试 \
    --KeyId 0397abd8-4029-11f0-aa65-52540064acab
```

Output: 
```
{
    "Response": {
        "DataKeyId": "eb46f9c0-5015-11f0-ace9-525400eb1719",
        "KeyId": "0397abd8-4029-11f0-aa65-52540064acab",
        "RequestId": "85568b48-a19c-43e1-9850-6d9101dc2b3a"
    }
}
```

