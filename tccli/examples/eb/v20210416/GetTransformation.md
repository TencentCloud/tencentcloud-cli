**Example 1: 获取转换器详情**



Input: 

```
tccli eb GetTransformation --cli-unfold-argument  \
    --EventBusId eb-xxxxx \
    --RuleId rule-xxxxxxxxx \
    --TransformationId tsfm-xxxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b7662cf2-ce20-4b3e-aff2-2cb875cf0b6b",
        "Transformations": [
            {
                "EtlFilter": {
                    "Filter": "{\"source\":\"ckafka.cloud.tencent\"}"
                },
                "Extraction": {
                    "ExtractionInputPath": "$",
                    "Format": "JSON",
                    "TextParams": {
                        "Separator": ","
                    }
                },
                "Transform": {
                    "OutputStructs": [
                        {
                            "Key": "age",
                            "Value": "$.age",
                            "ValueType": "NUMBER"
                        }
                    ]
                }
            }
        ]
    }
}
```

