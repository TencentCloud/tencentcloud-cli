**Example 1: 获取数据密钥的详情**



Input: 

```
tccli kms DescribeDataKey --cli-unfold-argument  \
    --DataKeyId c0fb30d1-4ceb-11f0-bcaa-525400eb1719
```

Output: 
```
{
    "Response": {
        "DataKeyMetadata": {
            "CreateTime": 1750323588,
            "CreatorUin": 100000007998,
            "DataKeyId": "c0fb30d1-4ceb-11f0-bcaa-525400eb1719",
            "DataKeyName": "42tofUJQy1gVjfsuIS0sbDoSqtpKuiw3",
            "DeletionDate": 0,
            "Description": "TestDateKey_01",
            "HsmClusterId": "",
            "KeyId": "0397abd8-4029-11f0-aa65-52540064acab",
            "KeyState": "Enabled",
            "NumberOfBytes": 1024,
            "Origin": "TENCENT_KMS",
            "Owner": "user",
            "ResourceId": "creatorUin/100000007998/c0fb30d1-4ceb-11f0-bcaa-525400eb1719"
        },
        "RequestId": "46107db0-5b2b-4d1d-b71d-acfefcaf6d12"
    }
}
```

