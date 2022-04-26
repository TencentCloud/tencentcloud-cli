**Example 1: 获取企业素材列表接口**



Input: 

```
tccli wav QueryMaterialList --cli-unfold-argument  \
    --Cursor +1H24tK0tELjSiTOR10DzA== \
    --Limit 100 \
    --MaterialType 0
```

Output: 
```
{
    "Response": {
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "PageData": [
            {
                "MaterialId": 0,
                "MaterialName": "素材名称",
                "Status": 0
            }
        ],
        "RequestId": "4d48312c-a062-4875-a5d5-69f0f11baf96"
    }
}
```

