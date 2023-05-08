**Example 1: 修改权重信息**



Input: 

```
tccli wedata ModifyDimensionWeight --cli-unfold-argument  \
    --ProjectId 1 \
    --WeightInfoList.0.QualityDim 1 \
    --WeightInfoList.0.Weight 0 \
    --Refresh True
```

Output: 
```
{
    "Response": {
        "RequestId": "f2a131b8-0de7-4cb8-a354-9bbfc5d3a028",
        "Data": true
    }
}
```

