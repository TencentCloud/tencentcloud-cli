**Example 1: 批量获取表元数据**



Input: 

```
tccli databuddy GetTables --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --FullNames my_catalog.my_schema.my_table
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tccatalog.v1.xxx",
                    "Name": "my_table"
                }
            ]
        }
    }
}
```

