**Example 1: 查询字段血缘**



Input: 

```
tccli wedata ListColumnLineage --cli-unfold-argument  \
    --TableUniqueId b4JSso6coG4BU96R-jkQEg
 \
    --Direction OUTPUT \
    --PageNumber 1 \
    --PageSize 10 \
    --ColumnName id \
    --Platform WEDATA
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageCount": 0,
            "PageNumber": 0,
            "PageSize": 0,
            "TotalCount": 0
        },
        "RequestId": "90da2b45-2ca8-48a3-9bc4-9ff1c9974da2"
    }
}
```

