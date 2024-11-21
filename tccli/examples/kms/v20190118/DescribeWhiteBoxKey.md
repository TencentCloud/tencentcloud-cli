**Example 1: 展示白盒密钥的信息**



Input: 

```
tccli kms DescribeWhiteBoxKey --cli-unfold-argument  \
    --KeyId 5551ef2e-6742-11ef-8133-525400b2f623
```

Output: 
```
{
    "Response": {
        "KeyInfo": {
            "Algorithm": "SM4",
            "Alias": "lzc2",
            "CreateTime": 1725072007,
            "CreatorUin": 700001224419,
            "DecryptKey": "AACAAAAACMD5WLv****+rt0t6Qgamj/FwS6qYFZWwp/M0wM00KwxUSp8P",
            "Description": "2",
            "DeviceFingerprintBind": false,
            "EncryptKey": "AACAAAAACMD5WLvPb4qY***rt0t6Qgamj/FwS6qYFZWwp/M0wM00KwxUSp8P",
            "KeyId": "5551ef2e-6742-11ef-8133-525400b2f623",
            "OwnerUin": 100000007998,
            "ResourceId": "creatorUin/700001224419/5551ef2e-6742-11ef-8133-525400b2f623",
            "Status": "Enabled"
        },
        "RequestId": "13b3e0ed-7d5e-4c6c-99ba-b334f02d7573"
    }
}
```

