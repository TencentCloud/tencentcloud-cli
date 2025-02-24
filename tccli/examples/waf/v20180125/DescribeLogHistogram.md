**Example 1: 获取日志分布直方图**

根据指定的检索条件，获取符合检索条件的日志分布直方图

Input: 

```
tccli waf DescribeLogHistogram --cli-unfold-argument  \
    --From 1685086740862 \
    --To 1685087640862 \
    --Interval 30000 \
    --TopicId 2e7b5c4d-1be3-484a-xxxx-8705adb56dcd \
    --Query  \
    --SyntaxRule 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 14,
        "Interval": 30000,
        "HistogramInfos": [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ],
        "RequestId": "4279ae1f-cbd6-438b-xxxx-6df5a8152afd",
        "Topics": null
    }
}
```

