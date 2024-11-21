**Example 1: 从某个日志开始查询新增的扫码日志**

在同步日志的场景，通常只需要定时同步新增的日志，指定上一次请求时最后一行ID即可（初次请求时可以传 0）
例如：AfterLogId = 100, 表示查 LogId > 100 的日志，在返回空数组时表示没有新的日志了

Input: 

```
tccli trp DescribeRawScanLogs --cli-unfold-argument  \
    --PageSize 100 \
    --PageNumber 1 \
    --AfterLogId 100
```

Output: 
```
{
    "Response": {
        "ScanLogs": [
            {
                "LogId": 101,
                "Openid": "g3ST2ZYcreGP9jpqgKHOjuB1e0GrlI0t",
                "CreateTime": "2024-10-30T07:16:21.265Z",
                "Code": "https://anxin.qq.com/q99j9ovp5c6sok7l5g",
                "CorpId": 10000,
                "MerchantId": "pn30msjjxwga",
                "ProductId": "97zu51y30awe",
                "BatchId": "20241022112952826",
                "Province": "广东省",
                "City": "深圳市",
                "District": "福田区"
            }
        ],
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

