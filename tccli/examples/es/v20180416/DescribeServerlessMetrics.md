**Example 1: 获取serverless space维度过去5min钟新增存储指标值**



Input: 

```
tccli es DescribeServerlessMetrics --cli-unfold-argument  \
    --SpaceId space-18jf9xxx \
    --IndexId index-xxxxxx \
    --MetricType Storage
```

Output: 
```
{
    "Response": {
        "RequestId": "30204658-3518-11ef-979c-52540xxxxx",
        "Storage": 2262158.88
    }
}
```

