**Example 1: 获取慢查询日志分析**



Input: 

```
tccli dcdb DescribeDBSlowLogAnalysis --cli-unfold-argument  \
    --InstanceId dcdbt-ige1a5k3 \
    --StartTime '2018-04-05 00:00:00' \
    --EndTime '2018-04-05 20:00:00' \
    --User test_slow \
    --CheckSum 17988922643135866314 \
    --Db test \
    --ShardId ' shard-g7mxngqu'
```

Output: 
```
{
    "Response": {
        "StartTime": "2018-04-05 11:30:23",
        "RequestId": "838e3c36-54d6-4262-981a-50e8746eace6",
        "Data": [
            1,
            1,
            0,
            0,
            0,
            0,
            3
        ],
        "Period": 0,
        "EndTime": "2018-04-05 14:35:46"
    }
}
```

