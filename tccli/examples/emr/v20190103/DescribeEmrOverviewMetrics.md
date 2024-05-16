**Example 1: 查询监控概览页指标数据**



Input: 

```
tccli emr DescribeEmrOverviewMetrics --cli-unfold-argument  \
    --Start 1572447652 \
    --End 1572448652 \
    --Downsample 1m-max \
    --Metric HDFS.NN.FILES.TOTAL \
    --InstanceId emr-bemcdx96 \
    --Tags "{\"type\":\"FilesTotal\"}"
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Metric": "abc",
                "First": 0,
                "Last": 0,
                "Interval": 0,
                "DataPoints": [
                    "abc"
                ],
                "Tags": {
                    "Unit": "abc",
                    "Type": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

