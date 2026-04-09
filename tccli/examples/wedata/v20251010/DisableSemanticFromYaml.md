**Example 1: DisableSemanticFromYaml**



Input: 

```
tccli wedata DisableSemanticFromYaml --cli-unfold-argument  \
    --YamlContent version: 1.0 
metrics:
  # 原子指标
  - name: "simple_metric_3" # 指标英文名
    description: "" #optional
    type: SIMPLE # 指标类型,原子指标
    # 只剩自定义配置
    type_params:
      model_ref: yaml_nq_1
      source_table: c4.wedata_dev.customer2  # 指标的来源表,catalogName.databaseName.tableName
      expr: "SUM(account_num)"
      time_dimension: nq_dim1 # 指标的时间维度标识 \
    --WorkspaceId 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "Dimensions": [],
            "Message": "操作成功，共处理1个配置项",
            "Metrics": [
                {
                    "ErrorMessage": "",
                    "Id": "1040",
                    "ItemType": "METRIC",
                    "Name": "simple_metric_3",
                    "OperationType": "OFFLINE",
                    "Success": true
                }
            ],
            "Success": true,
            "Summary": {
                "FailedCount": 0,
                "OperationType": "DISABLE",
                "SuccessCount": 1,
                "TotalItems": 1
            }
        },
        "RequestId": "09813272-901f-439f-9430-626601cafe5d"
    }
}
```

