**Example 1: 获取元数据业务信息示例**

获取元数据业务信息示例

Input: 

```
tccli wedata GetMetaBiz --cli-unfold-argument  \
    --MetaType CATALOG \
    --MetaIdentifier tccatalog.v1.uid2883043051864705593
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsFavorite": false,
            "Tags": []
        },
        "RequestId": "cef1cb80-d10a-4faf-b424-43d5ee8869b2"
    }
}
```

