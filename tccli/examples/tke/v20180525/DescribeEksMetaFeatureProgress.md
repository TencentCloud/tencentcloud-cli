**Example 1: 查询EKS集群开通跨租户弹性网卡开通状态**



Input: 

```
tccli tke DescribeEksMetaFeatureProgress --cli-unfold-argument  \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "232323-5ed9-4cb7-9194-a95e2cd45332",
        "Status": "succeeded"
    }
}
```

