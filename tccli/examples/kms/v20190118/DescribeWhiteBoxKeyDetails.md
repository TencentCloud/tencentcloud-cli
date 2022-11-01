**Example 1: 获取白盒密钥列表**



Input: 

```
tccli kms DescribeWhiteBoxKeyDetails --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "KeyInfos": [
            {
                "Status": "xx",
                "DecryptKey": "xx",
                "KeyId": "xx",
                "Description": "xx",
                "CreatorUin": 1,
                "ResourceId": "xx",
                "OwnerUin": 1,
                "Algorithm": "xx",
                "Alias": "xx",
                "EncryptKey": "xx",
                "CreateTime": 1,
                "DeviceFingerprintBind": true
            },
            {
                "Status": "xx",
                "DecryptKey": "xx",
                "KeyId": "xx",
                "Description": "xx",
                "CreatorUin": 1,
                "ResourceId": "xx",
                "OwnerUin": 1,
                "Algorithm": "xx",
                "Alias": "xx",
                "EncryptKey": "xx",
                "CreateTime": 1,
                "DeviceFingerprintBind": true
            }
        ],
        "TotalCount": 2,
        "RequestId": "xx"
    }
}
```

