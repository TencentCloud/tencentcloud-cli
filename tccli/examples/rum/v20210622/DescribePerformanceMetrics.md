**Example 1: 示例**



Input: 

```
tccli rum DescribePerformanceMetrics --cli-unfold-argument  \
    --AppId 1****7 \
    --StartTime 1778923333000 \
    --EndTime 1779182533000 \
    --Platform web \
    --Filters [{"Key":"normalized_page_url","Op"\:"in","Values":["商城首页"]}] \
    --Quantile 0.75
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"Filters JSON 解析失败: invalid character '\\\\\\\\' after object key\"}",
        "RequestId": "7811f99b-5837-4b2a-aa5b-6806c3cec284"
    }
}
```

