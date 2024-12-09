**Example 1: 上报自定义规则评估结果**

上报自定义规则评估结果

Input: 

```
tccli config PutEvaluations --cli-unfold-argument  \
    --ResultToken Wm9yZlY3WmlKa3cxaW1oQlu-H3WA6JZnH46cUAn2DWG**** \
    --Evaluations.0.ComplianceResourceId disk-26itbqha \
    --Evaluations.0.ComplianceResourceType QCS::CBS::Disk \
    --Evaluations.0.ComplianceRegion ap-guangzhou \
    --Evaluations.0.ComplianceType NON_COMPLIANT \
    --Evaluations.0.Annotation.Configuration 1 \
    --Evaluations.0.Annotation.DesiredValue 2 \
    --Evaluations.0.Annotation.Operator equal \
    --Evaluations.0.Annotation.Property age
```

Output: 
```
{
    "Response": {
        "RequestId": "d947eba9-f908-4d2e-9b3d-63bde43abd1a"
    }
}
```

