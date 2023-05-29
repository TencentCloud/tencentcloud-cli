**Example 1: 新建作业示例**

新建作业

Input: 

```
tccli oceanus CreateJob --cli-unfold-argument  \
    --Name job_new \
    --JobType 2 \
    --ClusterType 2 \
    --ClusterId cluster-xxxxxxxx \
    --CuMem 4 \
    --Remark 测试作业 \
    --FolderId folder-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "JobId": "cql-qlpn5o2a",
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dd08d16"
    }
}
```

