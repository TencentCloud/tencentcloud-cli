**Example 1: 获取模型可用的推理引擎列表**



Input: 

```
tccli dlc DescribeModelEngines --cli-unfold-argument  \
    --ModelUid m-xgboost-mao-6a2fc583-14cb
```

Output: 
```
{
    "Response": {
        "Engines": [
            {
                "Capabilities": {
                    "GpuOptional": true,
                    "SupportsParallelConfig": false,
                    "SupportsRemoteCode": false
                },
                "Description": "高性能梯度提升决策树框架，适用于表格数据分类与回归任务",
                "Enabled": true,
                "EngineId": "xgboost",
                "Exclusive": false,
                "ModelTypes": [
                    "ML"
                ],
                "Name": "XGBoost",
                "Tags": [
                    "表格数据"
                ],
                "Version": "v3.2.0"
            }
        ],
        "RequestId": "e2053422-9b23-4b0c-9b39-507b0c527f7f"
    }
}
```

