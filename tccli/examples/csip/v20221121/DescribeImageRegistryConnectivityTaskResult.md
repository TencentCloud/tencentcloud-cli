**Example 1: 查询镜像仓库联通性检查任务结果**



Input: 

```
tccli csip DescribeImageRegistryConnectivityTaskResult --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --TaskId 5a19ab3b-66a0-4f57-bad9-72c5cc17fc2f
```

Output: 
```
{
    "Response": {
        "ConnDetectResult": [],
        "Finished": 1,
        "RequestId": "d5a5bd41-3b86-448d-963c-3af4639c1783"
    }
}
```

