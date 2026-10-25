**Example 1: 1**



Input: 

```
tccli databuddy UpdateModelVersion --cli-unfold-argument  \
    --CatalogName marvin \
    --SchemaName abe \
    --ModelName hhhhhhaa \
    --ModelVersion 1 \
    --WorkspaceId 17678671667189298 \
    --AddedAliases ac \
    --RemovedAliases ab \
    --NewComment 该模型组织和管理相关数据内容，提供业务语义和技术定义。包含输入数据源、输出结果及特定算法类型。适用于数据分析团队进行业务洞察和决策支持等场景。2
```

Output: 
```
{
    "Response": {
        "Data": {
            "ModelVersion": {
                "Aliases": [
                    "ac"
                ],
                "AssetGuid": "tccatalog.v1.uid2125395121961709862@260073493_ap-guangzhou_MODEL_VERSION",
                "Audit": {
                    "CreatedAt": "1770100017934",
                    "Creator": "700002164619",
                    "CreatorName": "wedata30-test1@tencent.com",
                    "LastModifiedAt": "1787643835034",
                    "LastModifier": "700002164619",
                    "LastModifierName": "wedata30-test1@tencent.com"
                },
                "CatalogName": "",
                "Comment": "该模型组织和管理相关数据内容，提供业务语义和技术定义。包含输入数据源、输出结果及特定算法类型。适用于数据分析团队进行业务洞察和决策支持等场景。2",
                "ModelName": "",
                "Properties": [
                    {
                        "Key": "tclake.mlflow.copy_from",
                        "Value": "marvin.abe.m0119:4"
                    }
                ],
                "SchemaName": "",
                "Tags": [],
                "Uri": "cos://aa/bb/cc",
                "Version": "1"
            }
        },
        "RequestId": "c424cace-886b-4980-889a-9c8f7104a7ae"
    }
}
```

