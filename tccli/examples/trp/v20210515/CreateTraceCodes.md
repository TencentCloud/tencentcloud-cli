**Example 1: 批量将码和批次绑定**

批量将码和批次绑定并激活，会返回绑定后批次对应码的数量

Input: 

```
tccli trp CreateTraceCodes --cli-unfold-argument  \
    --BatchId xfetmgoiky2nms6nk8 \
    --Codes.0.Code https://anxin.m.qq.com/qr/eqdmnz7020bmtvi9_021351149823032923
```

Output: 
```
{
    "Response": {
        "BatchId": "abc",
        "ActiveCnt": 1,
        "CodeCnt": 1,
        "RequestId": "abc"
    }
}
```

