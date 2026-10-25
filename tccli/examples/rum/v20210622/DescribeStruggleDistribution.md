**Example 1: 示例**



Input: 

```
tccli rum DescribeStruggleDistribution --cli-unfold-argument  \
    --AppId 1****7 \
    --StartTime 1778916553000 \
    --EndTime 1779175753000 \
    --Platform web \
    --Filters [{"Key":"normalized_page_url","Op":"in","Values":["商品列表页"]}]
```

Output: 
```
{
    "Response": {
        "Result": "{\"Items\":[{\"Type\":\"back_forward\",\"Count\":26}],\"Total\":26}",
        "RequestId": "ac4681b0-1443-4ce3-87a8-42c16a220f8b"
    }
}
```

