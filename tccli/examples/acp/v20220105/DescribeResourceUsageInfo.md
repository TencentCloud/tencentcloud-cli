**Example 1: 获取当前用户资源使用情况**



Input: 

```
tccli acp DescribeResourceUsageInfo --cli-unfold-argument  \
    --PriceName sv_011886_testing_service_per_use
```

Output: 
```
{
    "Response": {
        "RequestId": "2950685b-6235-4e37-96c3-0238feb44c29",
        "Result": 0,
        "Data": {
            "ResourceName": "sv_011886_testing_service_per_use",
            "Total": 0,
            "UnusedCount": 0
        }
    }
}
```

