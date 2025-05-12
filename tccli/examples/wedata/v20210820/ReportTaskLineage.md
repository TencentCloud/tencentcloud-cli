**Example 1: 上报测试用例**



Input: 

```
tccli wedata ReportTaskLineage --cli-unfold-argument  \
    --ChannelType THIRD_REPORT \
    --Task.TaskId Task-001 \
    --Task.TaskType other \
    --Task.TaskSource other \
    --Task.ExtParams.0.Key param1 \
    --Task.ExtParams.0.Value value1 \
    --Task.ExtParams.1.Key param2 \
    --Task.ExtParams.1.Value value2 \
    --ProjectId 1486804694126882816 \
    --TableLineages.0.Sources.0.DatasourceId 61998 \
    --TableLineages.0.Sources.0.DatabaseName lineage_db1 \
    --TableLineages.0.Sources.0.TableName lineage_source_table1 \
    --TableLineages.0.Sources.0.CatalogName lineage_catalog1 \
    --TableLineages.0.Sources.0.TableType TABLE \
    --TableLineages.0.Sources.1.DatasourceId 61998 \
    --TableLineages.0.Sources.1.DatabaseName lineage_db2 \
    --TableLineages.0.Sources.1.TableName lineage_source_table2 \
    --TableLineages.0.Sources.1.CatalogName lineage_catalog1 \
    --TableLineages.0.Sources.1.TableType TABLE \
    --TableLineages.0.Sources.2.DatasourceId 61998 \
    --TableLineages.0.Sources.2.DatabaseName lineage_db2 \
    --TableLineages.0.Sources.2.TableName lineage_source_table3 \
    --TableLineages.0.Sources.2.CatalogName lineage_catalog1 \
    --TableLineages.0.Sources.2.TableType TABLE \
    --TableLineages.0.Target.DatasourceId 61998 \
    --TableLineages.0.Target.DatabaseName lineage_db3 \
    --TableLineages.0.Target.TableName lineage_target_table1 \
    --TableLineages.0.Target.CatalogName lineage_catalog1 \
    --TableLineages.0.Target.TableType TABLE \
    --TableLineages.1.Sources.0.DatasourceId 61999 \
    --TableLineages.1.Sources.0.DatabaseName lineage_db4 \
    --TableLineages.1.Sources.0.TableName lineage_source_table4 \
    --TableLineages.1.Sources.0.CatalogName lineage_catalog2 \
    --TableLineages.1.Sources.0.TableType TABLE \
    --TableLineages.1.Sources.1.DatasourceId 61999 \
    --TableLineages.1.Sources.1.DatabaseName lineage_db5 \
    --TableLineages.1.Sources.1.TableName lineage_source_table5 \
    --TableLineages.1.Sources.1.CatalogName lineage_catalog2 \
    --TableLineages.1.Sources.1.TableType TABLE \
    --TableLineages.1.Target.DatasourceId 61999 \
    --TableLineages.1.Target.DatabaseName lineage_db6 \
    --TableLineages.1.Target.TableName lineage_target_table2 \
    --TableLineages.1.Target.CatalogName lineage_catalog2 \
    --TableLineages.1.Target.TableType TABLE \
    --ColumnLineages.0.Sources.0.DatasourceId 61998 \
    --ColumnLineages.0.Sources.0.DatabaseName lineage_db1 \
    --ColumnLineages.0.Sources.0.TableName lineage_source_table1 \
    --ColumnLineages.0.Sources.0.CatalogName lineage_catalog1 \
    --ColumnLineages.0.Sources.0.TableType TABLE \
    --ColumnLineages.0.Sources.0.ColumnName source_column1 \
    --ColumnLineages.0.Sources.0.ColumnType STRING \
    --ColumnLineages.0.Target.DatasourceId 61998 \
    --ColumnLineages.0.Target.DatabaseName lineage_db3 \
    --ColumnLineages.0.Target.TableName lineage_target_table1 \
    --ColumnLineages.0.Target.ColumnName target_column1 \
    --ColumnLineages.0.Target.CatalogName lineage_catalog1 \
    --ColumnLineages.0.Target.TableType TABLE \
    --ColumnLineages.0.Target.ColumnType STRING
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

