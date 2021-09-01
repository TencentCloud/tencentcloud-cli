**Example 1: 查看服务版本历史**



Input: 

```
tccli tcb DescribeCloudBaseRunVersionSnapshot --cli-unfold-argument  \
    --EnvId lotestapi100004 \
    --ServerName test \
    --VersionName test-001 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "daaed203-3e79-4212-966f-55d7f98ac96e",
        "Snapshots": []
    }
}
```

