**Example 1: 获取数据密钥列表详情示例**



Input: 

```
tccli kms ListDataKeyDetail --cli-unfold-argument  \
    --SearchKeyAlias e6c1f360-4ceb-11f0-8428-52540073b995
```

Output: 
```
{
    "Response": {
        "DataKeyMetadatas": [
            {
                "CreateTime": 1750323652,
                "CreatorUin": 100000007998,
                "DataKeyId": "e6c1f360-4ceb-11f0-8428-52540073b995",
                "DataKeyName": "eY66EuC61oAhm6qXyjZAPWhX0Gn9oe8g",
                "DeletionDate": 1750928452,
                "Description": "TestDateKey_01",
                "HsmClusterId": "",
                "KeyId": "0397abd8-4029-11f0-aa65-52540064acab",
                "KeyState": "PendingDelete",
                "NumberOfBytes": 1024,
                "Origin": "TENCENT_KMS",
                "Owner": "user",
                "ResourceId": "creatorUin/100000007998/e6c1f360-4ceb-11f0-8428-52540073b995"
            }
        ],
        "RequestId": "75bd39cb-1e80-4b54-9b83-b991b6f684d6",
        "TotalCount": 1
    }
}
```

