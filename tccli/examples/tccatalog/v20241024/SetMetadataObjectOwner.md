**Example 1: 设置元数据对象所有者**



Input: 

```
tccli tccatalog SetMetadataObjectOwner --cli-unfold-argument  \
    --MetadataObjectType FUNCTION \
    --FullName layyu_lakehouse.s1.f2 \
    --OwnerType user \
    --OwnerName 700002180075
```

Output: 
```
{
    "Response": {
        "Set": true,
        "RequestId": "10fb8807-d818-410a-89af-2afa063b694f"
    }
}
```

