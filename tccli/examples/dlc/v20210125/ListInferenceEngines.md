**Example 1: 获取推理引擎列表（含元数据和能力声明）**



Input: 

```
tccli dlc ListInferenceEngines --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Capabilities": {
                    "GpuOptional": true,
                    "SupportsParallelConfig": false,
                    "SupportsRemoteCode": false
                },
                "Description": "Amazon Chronos-2 时间序列预测引擎，120M encoder-only 模型，支持多变量预测和协变量，CPU/GPU 部署",
                "Enabled": true,
                "EngineId": "chronos",
                "Exclusive": false,
                "ModelTypes": [
                    "TimeSeries"
                ],
                "Name": "Chronos-2",
                "Tags": [
                    "时间序列"
                ],
                "Version": "v2.0"
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 6,
        "TotalPages": 1,
        "RequestId": "c4dfe64b-e2ab-4653-a604-27c16455d4eb"
    }
}
```

