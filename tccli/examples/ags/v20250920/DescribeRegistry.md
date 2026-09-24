**Example 1: 查询 Registry 详情**

响应仅返回 Registry；已废弃顶层 RegistryId。

Input: 

```
tccli ags DescribeRegistry --cli-unfold-argument  \
    --RegistryId reg-0123abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Registry": {
            "RegistryId": "reg-0123abcd",
            "Name": "example-registry",
            "Description": "AGS 示例 Registry",
            "ApprovalMode": "MANUAL",
            "Region": "ap-guangzhou",
            "Status": "ACTIVE",
            "AppId": 1300000000,
            "CreatorUin": "100000000001",
            "CreatorSubAccountUin": "",
            "RecordCount": 3,
            "PublishedRecordCount": 1,
            "CreateTime": "2026-08-11T10:00:00Z",
            "UpdateTime": "2026-08-11T10:00:00Z",
            "Tags": []
        }
    }
}
```

