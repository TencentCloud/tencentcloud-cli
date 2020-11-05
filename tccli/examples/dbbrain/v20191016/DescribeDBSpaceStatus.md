**Example 1: Querying overview of instance space usage during a specified time period**



Input: 

```
tccli dbbrain DescribeDBSpaceStatus --cli-unfold-argument  \
    --InstanceId cdb-test\
    --RangeDays 5
```

Output: 
```
{
    "Response": {
        "Remain": 23224,
        "RequestId": "78cf7bb1-0608-11ea-a9ef-2736f0f7f829",
        "Growth": 231,
        "Total": 50000,
        "AvailableDays": 35
    }
}
```

