**Example 1: 示例**

获取数据库实例的全部非系统内置的DB列表。

Input: 

```
tccli dsgc QueryDSPAMetaResourceDbList --cli-unfold-argument  \
    --DspaId dspa-ab32dc78 \
    --ResourceId cdb-5bcpe42v \
    --ResourceRegion ap-guangzhou \
    --MetaType cdb
```

Output: 
```
{
    "Response": {
        "DbRelationStatusItems": [
            {
                "DbName": "test001",
                "BindStatus": "binded",
                "ValidStatus": "valid"
            }
        ],
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

