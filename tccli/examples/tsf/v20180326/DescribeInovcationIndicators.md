**Example 1: 查询调用监控指标**

1

Input: 

```
tccli tsf DescribeInovcationIndicators --cli-unfold-argument  \
    --Dimension service \
    --StartTime '2019-05-28 17:33:47' \
    --EndTime '2019-05-29 17:33:47' \
    --NamespaceId namespace-by8j6mak \
    --ServiceId ms-opy5kjy4
```

Output: 
```
{
    "Response": {
        "RequestId": "af44be89-38f9-4103-a6d1-0869e450012a",
        "Result": {
            "InvocationQuantity": null,
            "InvocationSuccessRate": null,
            "InvocationAvgDuration": null,
            "InvocationQuantityDistribution": null,
            "InvocationSuccessDistribution": null,
            "InvocationFailedDistribution": null,
            "InvocationStatusDistribution": null,
            "InvocationDurationDistribution": null
        }
    }
}
```

