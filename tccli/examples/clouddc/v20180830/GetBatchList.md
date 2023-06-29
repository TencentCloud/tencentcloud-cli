**Example 1: 获取批次列表**



Input: 

```
tccli clouddc GetBatchList --cli-unfold-argument  \
    --Page 123 \
    --PageSize 20 \
    --BatchName xx \
    --LeadReleaseSource xiaoshouyi \
    --LeadReleaseOriginMsg xx
```

Output: 
```
{
    "Response": {
        "JsonString": "{\"List\":[{\"AccountId\":\"1234\",\"BatchId\":1,\"BatchName\":\"mhy name22\",\"LeadReleaseSource\":\"\",\"LeadReleaseOriginMsg\":\"LeadReleaseOrigin Msg\",\"UpdateTime\":\"2021-03-15 17:51:11\",\"CreateTime\":\"2021-03-15 17:51:11\"}],\"Total\":1}",
        "RequestId": "25ede15b-f30e-4f5f-8356-c38db98cfa23"
    }
}
```

