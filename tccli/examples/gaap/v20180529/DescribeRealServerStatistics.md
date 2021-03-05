**Example 1: 查询已绑定源站健康检查统计数据**

查询已绑定源站健康检查统计数据

Input: 

```
tccli gaap DescribeRealServerStatistics --cli-unfold-argument  \
    --RealServerId rs-rfgt56hy \
    --ListenerId listener-gucvb6d \
    --WithinTime 3
```

Output: 
```
{
    "Response": {
        "StatisticsData": [
            {},
            {}
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

