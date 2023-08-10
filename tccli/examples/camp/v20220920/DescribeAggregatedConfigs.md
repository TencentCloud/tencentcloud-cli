**Example 1: DescribeAggregatedConfigs**

拉取配置聚合信息

Input: 

```
tccli camp DescribeAggregatedConfigs --cli-unfold-argument  \
    --Platform abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Query abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "AggregatedConfigs": [
            {
                "ProjectID": "abc",
                "ConfigName": "abc",
                "ConfigType": "abc",
                "VersionCount": 0
            }
        ],
        "TotalCount": 1,
        "Filters": [
            {
                "Name": "abc",
                "Values": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

