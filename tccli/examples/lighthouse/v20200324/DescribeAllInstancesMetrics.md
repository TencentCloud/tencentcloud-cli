**Example 1: 查询用户全地域实例的最大到期时间**



Input: 

```
tccli lighthouse DescribeAllInstancesMetrics --cli-unfold-argument  \
    --Filters.0.Name bundle-type \
    --Filters.0.Values RAZOR_SPEED_BUNDLE \
    --Metrics MaxExpiredTime \
    --Uins 100000001
```

Output: 
```
{
    "Response": {
        "RequestId": "14e4cb2b-cf4a-4d8b-a0d5-44341cf97f34",
        "UserMetricResults": [
            {
                "Uin": "100000001",
                "MetricResults": [
                    {
                        "Name": "MaxExpiredTime",
                        "Values": [
                            "2024-12-16 22:10:44"
                        ]
                    }
                ]
            }
        ]
    }
}
```

