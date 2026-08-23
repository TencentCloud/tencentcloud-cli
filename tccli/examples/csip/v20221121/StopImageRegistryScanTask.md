**Example 1: 停止镜像仓库镜像扫描任务**



Input: 

```
tccli csip StopImageRegistryScanTask --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --ImageId 3389 \
    --TaskId 2040
```

Output: 
```
{
    "Response": {
        "RequestId": "5a42ec41-0e6a-4e67-b8ab-45d53616095f"
    }
}
```

