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

**Example 2: 获取漏洞扫描资源使用情况**



Input: 

```
tccli acp DescribeResourceUsageInfo --cli-unfold-argument  \
    --Platform 0 \
    --Source 3 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5251f818-f384-49f0-8681-d4dba6d12826",
        "Result": 0,
        "Data": {
            "ResourceName": "sv_011886_keen_p",
            "Total": 0,
            "UnusedCount": 0
        }
    }
}
```

**Example 3: 获取应用合规基础版资源使用情况**



Input: 

```
tccli acp DescribeResourceUsageInfo --cli-unfold-argument  \
    --Platform 0 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4e417380-6596-4e49-b1eb-ac96d567ae0f",
        "Result": 0,
        "Data": {
            "ResourceName": "sv_011886_ab_p",
            "Total": 0,
            "UnusedCount": 0
        }
    }
}
```

