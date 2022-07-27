**Example 1: 新建发函**



Input: 

```
tccli bma CreateCRRight --cli-unfold-argument  \
    --ValidStartDate xx \
    --ValidEndDate xx \
    --WorkId 0 \
    --TortUrl xx \
    --RightUrl xx \
    --TortTitle xx \
    --TortPlat xx \
    --FileUrl xx \
    --IsProducer xx
```

Output: 
```
{
    "Response": {
        "TortId": 0,
        "TortNum": "xx",
        "RequestId": "xx"
    }
}
```

