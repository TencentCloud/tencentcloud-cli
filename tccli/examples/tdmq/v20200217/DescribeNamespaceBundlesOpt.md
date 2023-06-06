**Example 1: test**

测试

Input: 

```
tccli tdmq DescribeNamespaceBundlesOpt --cli-unfold-argument  \
    --ClusterName tdmq_txy_gz_01 \
    --Limit 20 \
    --NamespaceName ns_1 \
    --NeedMetrics True \
    --Offset 0 \
    --TenantId pulsar-pbkdk57xz9wv
```

Output: 
```
{
    "Response": {
        "RequestId": "d2d3e253-3b1d-4471-a350-25e6ae20916c",
        "TotalCount": 30,
        "BundleSet": [
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
        ]
    }
}
```

