**Example 1: 删除表**

删除表

Input: 

```
tccli wedata DeleteTable --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --TableName create_table_2
```

Output: 
```
{
    "Response": {
        "RequestId": "8ff5a1ae-2931-4940-8ee4-18c5414143b6",
        "Data": {
            "Result": true
        }
    }
}
```

