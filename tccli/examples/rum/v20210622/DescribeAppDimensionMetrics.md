**Example 1: 查询多维分析数据**



Input: 

```
tccli rum DescribeAppDimensionMetrics --cli-unfold-argument  \
    --Filter '[]' \
    --ProjectID 1 \
    --FilterSimple '{\"entrance_time__gte\":1671367462000,\"entrance_time__lte\":1671453862000,\"category__in\":[\"PERF_NET_REQUEST\"],\"d4\":\"false\",\"d3\":\"http\",\"v1__lte\":300000}' \
    --From 'kv_7_dist' \
    --Fields '[[\"explodeDimensions\",\"d2\",\"d8\"],[\"as\",[\"multiIf\",[\"equals\",\"dimension_name\",\"'d2'\"],\"'domain'\",[\"equals\",\"dimension_name\",\"'d8'\"],\"'region'\",\"dimension_name\"],\"dimension\"],[\"as\",[\"avg\",\"v1\"],\"cost_time\"],[\"as\",[\"count\",1],\"request_cnt\"],[\"as\",[\"aggByPartition\",\"sum\",\"request_cnt\",\"dimension_name\"],\"total_request_cnt\"],[\"as\",\"total_request_cnt\",\"total_cnt\"],[\"as\",\"request_cnt\",\"cnt\"],[\"as\",[\"aggByPartition\",\"row_number\",\"none\",\"dimension_name\",[\"order_by\",\"request_cnt\",\"desc\"]],\"rank_cnt\"]]' \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "Data": "'{\"status\":\"ok\",\"code\":10000,\"msg\":\"ok\",\"data\":[{\"by_dimension\":[\"d2\",\"m.zhipin.com\"],\"cnt\":1280,\"cost_time\":1480,\"dimension\":\"domain\",\"dimension_name\":\"d2\",\"dimension_value\":\"m.zhipin.com\",\"rank_cnt\":1,\"request_cnt\":1280,\"total_cnt\":1280,\"total_request_cnt\":1280},{\"by_dimension\":[\"d8\",\"unsupported\"],\"cnt\":1280,\"cost_time\":1480,\"dimension\":\"region\",\"dimension_name\":\"d8\",\"dimension_value\":\"unsupported\",\"rank_cnt\":1,\"request_cnt\":1280,\"total_cnt\":1280,\"total_request_cnt\":1280}]}'",
        "RequestId": "8a211fc4-7ce2-40ce-ad49-1c29cca2f3fc"
    }
}
```

