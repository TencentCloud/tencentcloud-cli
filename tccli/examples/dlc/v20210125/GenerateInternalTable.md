**Example 1: GenerateInternalTable**



Input: 

```
tccli dlc GenerateInternalTable --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName danielyyang \
    --TableBaseInfo.TableName myqqw \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --Columns.0.Name id \
    --Columns.0.Type string \
    --Columns.0.Comment id \
    --Properties.0.Key write.upsert.enabled \
    --Properties.0.Value true \
    --UpsertKeys id
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "CREATE TABLE IF NOT EXISTS `DataLakeCatalog`.`danielyyang`.`myqqw` (\n`id` string COMMENT 'id')\nPARTITIONED BY (bucket(4, `id`))\nTBLPROPERTIES ('format-version'='2', 'write.upsert.enabled'='true', 'write.update.mode'='merge-on-read', 'write.merge.mode'='merge-on-read', 'write.parquet.bloom-filter-enabled.column.id'='true', 'dlc.ao.data.govern.sorted.keys'='id', 'write.metadata.delete-after-commit.enabled'='true', 'write.metadata.previous-versions-max'='100', 'write.metadata.metrics.default'='full');"
        },
        "IsTIcebergSql": false,
        "RequestId": "e67bf71c-8117-40d9-9d6c-28468eeec3d8"
    }
}
```

