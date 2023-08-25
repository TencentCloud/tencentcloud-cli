**Example 1: 获取扫描结果数据样本**



Input: 

```
tccli dsgc DescribeDSPATaskResultDataSample --cli-unfold-argument  \
    --DspaId dspa-001 \
    --FieldResultId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "Items": [
            {
                "DataSample": "test"
            }
        ]
    }
}
```

