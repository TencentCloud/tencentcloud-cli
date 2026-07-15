**Example 1: 测试数据**



Input: 

```
tccli waf DescribeHistogram --cli-unfold-argument  \
    --FromTime 2026-02-03 00:00:00 \
    --ToTime 2026-02-03 20:00:00 \
    --QueryField ip \
    --Source access
```

Output: 
```
{
    "Response": {
        "Histogram": [
            "{\"count\":200,\"ip\":\"222.12.11.104\"}"
        ],
        "RequestId": "26b5b437-b2a1-4019-b06d-37e7fdfd460d"
    }
}
```

