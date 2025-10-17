**Example 1: 查询表的所有列元数据**



Input: 

```
tccli wedata DescribeColumnsMeta --cli-unfold-argument  \
    --PageNumber 1 \
    --TableId JqDviGd3SJKP1DzlUXXNEA \
    --PageSize 5 \
    --IsPartitionQuery False
```

Output: 
```
{
    "Response": {
        "ColumnMetaSet": [
            {
                "ColumnFamiliesFieldSet": [],
                "Description": null,
                "DictionaryId": null,
                "DictionaryName": null,
                "IsPartition": false,
                "LevelName": null,
                "LevelRank": null,
                "Name": "cloa",
                "NameCn": null,
                "NameEn": null,
                "Position": 0,
                "Type": "int"
            },
            {
                "ColumnFamiliesFieldSet": [],
                "Description": null,
                "DictionaryId": null,
                "DictionaryName": null,
                "IsPartition": false,
                "LevelName": null,
                "LevelRank": null,
                "Name": "colb",
                "NameCn": null,
                "NameEn": null,
                "Position": 1,
                "Type": "string"
            }
        ],
        "RequestId": "5c2475a9-a65a-4c74-b672-b1e2a4bbc1bd",
        "TotalCount": 2
    }
}
```

