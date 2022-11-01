**Example 1: 列举服务组下的接口**



Input: 

```
tccli tione DescribeAPIConfigs --cli-unfold-argument  \
    --Filters.0.Name ServiceGroupId \
    --Filters.0.Values ms-xxxx
```

Output: 
```
{
    "Response": {
        "Details": [],
        "TotalCount": 0,
        "RequestId": "3b4b735f-2d89-43b3-b6d5-8efb4143daa6"
    }
}
```

