**Example 1: 批量将码和批次绑定**

批量将码和批次绑定并激活，会返回绑定后批次对应码的数量

Input: 

```
tccli trp CreateTraceCodes --cli-unfold-argument  \
    --BatchId 20241022112952826 \
    --Codes.0.Code https://anxin.m.qq.com/qr/eqdmnz7020bmtvi9_021351149823032923
```

Output: 
```
{
    "Response": {
        "BatchId": "20241022112952826",
        "ActiveCnt": 1,
        "CodeCnt": 1,
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

