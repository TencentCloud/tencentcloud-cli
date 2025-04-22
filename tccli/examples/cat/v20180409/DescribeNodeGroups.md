**Example 1: 获取拨测点组**

获取拨测点组


Input: 

```
tccli cat DescribeNodeGroups --cli-unfold-argument  \
    --RegionID 1 \
    --NetServiceID 99
```

Output: 
```
{
    "Response": {
        "RequestId": "fyy3-g7ujmxbouxshy3plmkmhlnmdbfh"
    }
}
```

**Example 2: 获取定时任务拨测点组**

获取定时任务中网络质量任务类型，PC类任务的可用性拨测点组

Input: 

```
tccli cat DescribeNodeGroups --cli-unfold-argument  \
    --NodeGroupType 1 \
    --IPType 0 \
    --NodeType 1 \
    --TaskType 5 \
    --ProbeType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3ea82ed9-5901-4c69-b5e2-c4c84c9538e5"
    }
}
```

**Example 3: 获取即时拨测拨测点组**

获取即时拨测任务中网络质量任务类型，PC类任务的精选拨测点组

Input: 

```
tccli cat DescribeNodeGroups --cli-unfold-argument  \
    --NodeGroupType 0 \
    --TaskCategory 1 \
    --IPType 0 \
    --NodeType 1 2 \
    --TaskType 5 \
    --ProbeType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "248cfe54-6cb6-46c7-b73d-9c78108add00"
    }
}
```

