**Example 1: 删除表**



Input: 

```
tccli dlc DeleteTable --cli-unfold-argument  \
    --TableBaseInfo.TableName abc \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableBaseInfo.DatabaseName db
```

Output: 
```
{
    "Response": {
        "RequestId": "b076c1df-26f0-45b7-84f1-fa4eeca7c83f"
    }
}
```

