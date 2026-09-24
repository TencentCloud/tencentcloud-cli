**Example 1: 更新 Registry 描述**

只允许修改 Description；Name/ApprovalMode 不可修改。

Input: 

```
tccli ags UpdateRegistry --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --Description 更新后的描述
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Registry": {
            "RegistryId": "reg-0123abcd",
            "Name": "example-registry",
            "Description": "更新后的描述",
            "ApprovalMode": "MANUAL",
            "Region": "ap-guangzhou",
            "Status": "ACTIVE",
            "AppId": 1300000000,
            "CreatorUin": "100000000001",
            "CreatorSubAccountUin": "",
            "RecordCount": 3,
            "PublishedRecordCount": 1,
            "CreateTime": "2026-08-11T10:00:00Z",
            "UpdateTime": "2026-08-11T12:00:00Z",
            "Tags": []
        }
    }
}
```

