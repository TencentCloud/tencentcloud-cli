**Example 1: CopyCryptoColumnPolicy**



Input: 

```
tccli casb CopyCryptoColumnPolicy --cli-unfold-argument  \
    --CasbId casb-1 \
    --MetaDataId meta-1 \
    --DstCasbId casb-1 \
    --DstMetaDataId meta-2
```

Output: 
```
{
    "Response": {
        "RequestId": "1f7310c2-5459-460f-a56d-2e7d501c8313"
    }
}
```

**Example 2: 复制同一数据库实例不同DB的表策略**



Input: 

```
tccli casb CopyCryptoColumnPolicy --cli-unfold-argument  \
    --DstDatabaseName casbtest0 \
    --CasbId casb-mln08msg \
    --DstMetaDataId metadata-ea1lr450 \
    --MetaDataId metadata-ea1lr450 \
    --SrcTableFilter.0.TableNameSet beian_subject \
    --SrcTableFilter.0.DatabaseName casb \
    --DstCasbId casb-mln08msg
```

Output: 
```
{
    "Response": {
        "RequestId": "b6474d57-6002-4c7a-a0a3-16fc83b6a309"
    }
}
```

