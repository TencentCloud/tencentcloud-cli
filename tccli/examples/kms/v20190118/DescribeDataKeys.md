**Example 1: 获取数据密钥的详情列表示例**



Input: 

```
tccli kms DescribeDataKeys --cli-unfold-argument  \
    --DataKeyIds 7fe31abf-5018-11f0-b672-52540073b995 8042dfcb-5018-11f0-b672-52540073b995
```

Output: 
```
{
    "Response": {
        "DataKeyMetadatas": [
            {
                "CreateTime": 1750672660,
                "CreatorUin": 100000007998,
                "DataKeyId": "7fe31abf-5018-11f0-b672-52540073b995",
                "DataKeyName": "Test6331120",
                "DeletionDate": 0,
                "Description": "",
                "HsmClusterId": "",
                "KeyId": "0397abd8-4029-11f0-aa65-52540064acab",
                "KeyState": "Enabled",
                "NumberOfBytes": 32,
                "Origin": "EXTERNAL",
                "Owner": "user",
                "ResourceId": "creatorUin/100000007998/7fe31abf-5018-11f0-b672-52540073b995"
            },
            {
                "CreateTime": 1750672660,
                "CreatorUin": 100000007998,
                "DataKeyId": "8042dfcb-5018-11f0-b672-52540073b995",
                "DataKeyName": "miNAmDEc09znOK7jw9Yi3L9cmq8xk6z1",
                "DeletionDate": 0,
                "Description": "TestDateKey_01",
                "HsmClusterId": "",
                "KeyId": "0397abd8-4029-11f0-aa65-52540064acab",
                "KeyState": "Enabled",
                "NumberOfBytes": 1024,
                "Origin": "TENCENT_KMS",
                "Owner": "user",
                "ResourceId": "creatorUin/100000007998/8042dfcb-5018-11f0-b672-52540073b995"
            }
        ],
        "RequestId": "33c0c722-09e0-4f19-b16b-187a5898fd66"
    }
}
```

