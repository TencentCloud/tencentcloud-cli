**Example 1: 查看资源关联的标签**



Input: 

```
tccli tag DescribeResourceTagsByResourceIdsSeq --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourcePrefix instance \
    --ResourceRegion ap-guangzhou \
    --ResourceIds ins-1234
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Offset": 0,
        "Limit": 15,
        "Tags": [
            {
                "ServiceType": "cvm",
                "TagKey": "key1",
                "TagValue": "val1",
                "TagKeyMd5": "cc4dd1da7e1a754534215f02fb9ba85d",
                "TagValueMd5": "cc4dd1da7e1a754534215f02fb9ba85d",
                "ResourceId": "ins-1234"
            }
        ],
        "RequestId": "34bdd6cc-34b0-4ef4-9051-be9a5294be8e"
    }
}
```

