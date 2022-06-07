**Example 1: 批量导入二维码**



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
        "BatchId": "xx",
        "ActiveCnt": 1,
        "RequestId": "xx",
        "CodeCnt": 1
    }
}
```

