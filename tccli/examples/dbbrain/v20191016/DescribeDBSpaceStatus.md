**Example 1: 获取指定时间段内的实例空间使用概览**

获取指定时间段内的实例空间使用概览。

Input: 

```
tccli dbbrain DescribeDBSpaceStatus --cli-unfold-argument  \
    --InstanceId cdb-test \
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

