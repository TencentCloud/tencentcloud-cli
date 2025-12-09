**Example 1: 获取对象存储上传密钥**



Input: 

```
tccli lke DescribeStorageCredential --cli-unfold-argument  \
    --BotBizId 1727231073371148288
```

Output: 
```
{
    "Response": {
        "Bucket": "qidian-qbot-test-1251316161",
        "CorpUin": "0",
        "Credentials": {
            "TmpSecretId": "***************************************************",
            "TmpSecretKey": "***************************************************",
            "Token": "***************************************************"
        },
        "ExpiredTime": 1701429243,
        "FilePath": "/corp/137/doc/",
        "Region": "ap-guangzhou",
        "RequestId": "87d578f9-6de5-4515-906e-d28e56d33fe0",
        "StartTime": 1701425643,
        "Type": "cos"
    }
}
```

**Example 2: 获取文档上传密钥**

离线文档

Input: 

```
tccli lke DescribeStorageCredential --cli-unfold-argument  \
    --BotBizId 1779863007508561920 \
    --FileType md \
    --TypeKey offline
```

Output: 
```
{
    "Response": {
        "Bucket": "qidian-qbot-test-1251316161",
        "CorpUin": "0",
        "Credentials": {
            "TmpSecretId": "*****************************************",
            "TmpSecretKey": "***************************************",
            "Token": "*******************************************************"
        },
        "ExpiredTime": 1717063483,
        "FilePath": "",
        "ImagePath": "",
        "Region": "ap-guangzhou",
        "RequestId": "11b8fa96-4700-4f11-8eb0-421de37ed48d",
        "StartTime": 1717062883,
        "Type": "cos",
        "UploadPath": "/corp/1737374499879124992/1779863007508561920/doc/QUiGRdWFAFBkDKjhuxbd-1796118032488595456.md"
    }
}
```

