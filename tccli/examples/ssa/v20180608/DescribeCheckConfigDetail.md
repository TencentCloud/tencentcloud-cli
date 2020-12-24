**Example 1: 云安全配置检查项详情**



Input: 

```
tccli ssa DescribeCheckConfigDetail --cli-unfold-argument  \
    --Id ins-iermc23
```

Output: 
```
{
    "Response": {
        "CheckConfigDetail": {
            "Id": "17a5c13d-f95d-4065-8e7d-33b6b56e71b5",
            "ErrorCount": 0,
            "NameEn": "check_cos_bucket_acl",
            "SafeCount": 66,
            "IgnoreCount": 4,
            "ResCount": 100,
            "RiskCount": 30,
            "CheckName": "COS-Bucket权限设置",
            "Method": "进入腾讯云“控制台-对象存储-存储桶列表”找到开放了公有读写权限的桶或者公有读私有写权限的桶，确认是否符合预期，对不需要开放匿名读写的桶设置为私有读写权限。",
            "Doc": "https://cloud.tencent.com/document/product/436/13315",
            "Content": "存储桶的公有读和公有写权限可以通过匿名身份直接读取和写入存储桶中的数据，存在一定的安全风险。为确保您的数据安全，不推荐将存储通权限设置为公有读写或公有读私有写，建议您选择私有读写权限.",
            "AssetType": "cos",
            "IsPass": 2,
            "IsIgnore": 0
        },
        "RequestId": "d4d1e94d-430e-4bc7-9c10-a84f0685e366"
    }
}
```

