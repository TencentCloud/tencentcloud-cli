**Example 1: 获取白盒密钥列表**



Input: 

```
tccli kms DescribeWhiteBoxKeyDetails --cli-unfold-argument  \
    --KeyStatus 1 \
    --Offset 0 \
    --Limit 1 \
    --TagFilters.0.TagKey env \
    --TagFilters.0.TagValue dev
```

Output: 
```
{
    "Response": {
        "KeyInfos": [
            {
                "Algorithm": "SM4",
                "Alias": "testKey1",
                "CreateTime": 1730441467,
                "CreatorUin": 700001224419,
                "DecryptKey": "AACAAAAA3iht+5vrtKBnOagzrjeMFY8GZnRWIOgNcaKtY4RzWUmt0chcuELNIt6ZADmXSEdfndSWfAKizW1F4rnp2fncVQppWNlDjSwY6F/RcSCmU0/aDx3Yc2UIq/zM1jsLFX29CUBQD2a1pNzwepAl1A5HbxLYnrwVdB8Z364d9CyNd5YhVUKo4a8vmx0KA66SaLFSlzpWNZWAb+kZGrJDWMMRqLYigukAYDPsPYXMAb/MIoW5ywicGiY04vI59J1LVPezyMhi5ydTHuImNEcgYw2Tt07yG7LiDFVkWo5iCXXX9/zu+9eXdX93WGz20oDDBwpcFsKMk9tXvVhx7o9TCSgT7VERIQOWQKTH9iDb5RUyRPqPvyV1KEtbhTx/AlnkZEIdOM411JIvNucskvES4RaZ/MS+wxhkUYnFjL6GMg4MLepB87QaA7zivBKc",
                "Description": "测试描述信息",
                "DeviceFingerprintBind": false,
                "EncryptKey": "AACAAAAA3iht+5vrtKBnOagzrjeMFY8GZnRWIOgNcaKtY4RzWUmt0chcuELNIt6ZADmXSEdfndSWfAKizW1F4rnp2fncVQppWNlDjSwY6F/RcSCmU0/aDx3Yc2UIq/zM1jsLFX29CUBQD2a1pNzwepAl1A5HbxLYnrwVdB8Z364d9CyNd5YhVUKo4a8vmx0KA66SaLFSlzpWNZWAb+kZGrJDWMMRqLYigukAYDPsPYXMAb/MIoW5ywicGiY04vI59J1LVPezyMhi5ydTHuImNEcgYw2Tt07yG7LiDFVkWo5iCXXX9/zu+9eXdX93WGz20oDDBwpcFsKMk9tXvVhx7o9TCSgT7VERIQOWQKTH9iDb5RUyRPqPvyV1KEtbhTx/AlnkZEIdOM411JIvNucskvES4RaZ/MS+wxhkUYnFjL6GMg4MLepB87QaA7zivBKc",
                "KeyId": "14a9885b-9818-11ef-8d67-5254008ae90d",
                "OwnerUin": 100000007998,
                "ResourceId": "creatorUin/700001224419/14a9885b-9818-11ef-8d67-5254008ae90d",
                "Status": "Enabled"
            }
        ],
        "RequestId": "052e4c07-795b-4aa1-8b8f-b968d3792dea",
        "TotalCount": 4
    }
}
```

