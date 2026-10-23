**Example 1: 查询指定站点一段时间范围内日志分析按缓存状态分组的统计结果**

查询站点（ZoneId = zone-3qcox8or8ccl）中国大陆的七层访问日志在 2026-07-14T00:00:00Z ～ 2026-07-18T00:00:00Z 的统计结果，统计语句是: select EdgeCacheStatus as status, count(*) as cnt group by status limit 2，过滤条件是 缓存状态 = 未命中 或 其他。

Input: 

```
tccli teo DescribeLogAnalysisStatistics --cli-unfold-argument  \
    --ZoneId zone-3qcox8or8ccl \
    --Area mainland \
    --LogType l7-access-logs \
    --StartTime 2026-07-14T00:00:00Z \
    --EndTime 2026-07-18T00:00:00Z \
    --Query ${EdgeCacheStatus} in ['miss','other'] | select EdgeCacheStatus as status, count(*) as cnt group by status limit 2
```

Output: 
```
{
    "Response": {
        "Columns": [
            "status"
        ],
        "Records": [
            {
                "Record": [
                    "miss"
                ]
            }
        ],
        "RequestId": "6d5d22a3-7977-4fb9-b649-c796fd9cf358"
    }
}
```

**Example 2: 查询指定站点一段时间范围内日志分析日志总数**

查询站点（ZoneId = zone-3qcox8or8ccl）中国大陆的七层访问日志在 2026-07-14T00:00:00Z ～ 2026-07-18T00:00:00Z 的统计结果，统计语句是: select count(*) as cnt，无过滤条件。

Input: 

```
tccli teo DescribeLogAnalysisStatistics --cli-unfold-argument  \
    --ZoneId zone-3qcox8or8ccl \
    --Area mainland \
    --LogType l7-access-logs \
    --StartTime 2026-07-14T00:00:00Z \
    --EndTime 2026-07-18T00:00:00Z \
    --Query * | select count(*) as cnt
```

Output: 
```
{
    "Response": {
        "Columns": [
            "cnt"
        ],
        "Records": [
            {
                "Record": [
                    "5"
                ]
            }
        ],
        "RequestId": "d3c0b5e3-b3fa-433e-97e5-9274c5d3167f"
    }
}
```

