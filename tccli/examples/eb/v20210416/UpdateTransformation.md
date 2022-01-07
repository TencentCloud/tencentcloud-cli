**Example 1: 更新转换器**



Input: 

```
tccli eb UpdateTransformation --cli-unfold-argument  \
    --EventBusId eb-xxxxx \
    --RuleId rule-xxxxx \
    --TransformationId tsfm-xxxxx \
    --Transformations.0.Extraction.ExtractionInputPath $ \
    --Transformations.0.Extraction.Format JSON \
    --Transformations.0.EtlFilter.Filter {"source":"ckafka.cloud.tencent"} \
    --Transformations.0.Transform.OutputStructs.0.Key data \
    --Transformations.0.Transform.OutputStructs.0.Value $.data \
    --Transformations.0.Transform.OutputStructs.0.ValueType STRING \
    --Transformations.0.Transform.OutputStructs.1.Key age \
    --Transformations.0.Transform.OutputStructs.1.Value $.age \
    --Transformations.0.Transform.OutputStructs.1.ValueType NUMBER
```

Output: 
```
{
    "Response": {
        "RequestId": "e3d43926-c2cd-49f2-97f0-53db21e6fcea"
    }
}
```

