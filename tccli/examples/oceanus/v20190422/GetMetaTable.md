**Example 1: 查询元数据表信息**



Input: 

```
tccli oceanus GetMetaTable --cli-unfold-argument  \
    --Catalog _dc \
    --Database _db \
    --Table my_table1 \
    --WorkSpaceId space-xxx
```

Output: 
```
{
    "Response": {
        "SerialId": "mtable-7v16heof",
        "Catalog": "_dc",
        "Database": "_db",
        "Table": "my_table1",
        "DDL": "Q1JFQVRFIFRBQkxFIGRhdGFnZW5fc291cmNlX3RhYmxlICggCiAgICBpZCBJTlQsIAogICAgbmFtZSBTVFJJTkcgCikgV0lUSCAoCidjb25uZWN0b3InPSdkYXRhZ2VuJywKJ3Jvd3MtcGVyLXNlY29uZCcgPSAnMScKKTs=",
        "CreateTime": "2023-11-08 14:45:07",
        "RequestId": "6d1f41df-7c10-4ddd-a6e0-e05bccd996fa"
    }
}
```

