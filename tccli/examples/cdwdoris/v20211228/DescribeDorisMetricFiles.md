**Example 1: DescribeDorisMetricFiles**



Input: 

```
tccli cdwdoris DescribeDorisMetricFiles --cli-unfold-argument  \
    --ApiType abc \
    --DescribeMetricsFileReq.InstanceType abc \
    --DescribeMetricsFileReq.MetricType abc \
    --DescribeMetricsFileReq.IfAttention 0 \
    --ModifyMetricFileReq.Id 0 \
    --ModifyMetricFileReq.IfAttention abc \
    --InstanceId abc \
    --ModifyAttentionMetricFileReq.InstanceType abc \
    --ModifyAttentionMetricFileReq.MetricType abc \
    --ModifyAttentionMetricFileReq.Name abc \
    --ModifyAttentionMetricFileReq.IfAttention 0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "ReturnData": "abc",
        "RequestId": "abc"
    }
}
```

