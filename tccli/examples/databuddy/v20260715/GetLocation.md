**Example 1: 查询存储位置详情**

根据存储位置名获取单个存储位置的详细信息

Input: 

```
tccli databuddy GetLocation --cli-unfold-argument  \
    --LocationName test_1 \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Location": {
                "LocationName": "test_1",
                "LocationUri": "cos://bucket-30-251436191",
                "Comment": "test comment",
                "Properties": [],
                "Audit": {
                    "Creator": "700002164618",
                    "LastModifier": "700002164618",
                    "CreatedAt": "1776307158970",
                    "LastModifiedAt": "1785843769668"
                }
            }
        },
        "RequestId": "5e78a312-212a-4108-9c18-39d4c5ad0ec0"
    }
}
```

