**Example 1: 新建拦截**



Input: 

```
tccli bma CreateCRBlock --cli-unfold-argument  \
    --ValidStartDate xx \
    --ValidEndDate xx \
    --WorkId 0 \
    --TortUrl xx \
    --TortTitle xx \
    --TortPlat xx \
    --FileUrl xx \
    --BlockUrl xx
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

