**Example 1: 创建作业**

创建作业

Input: 

```
tccli oceanus CreateJob --cli-unfold-argument  \
    --Name create_job_test \
    --JobType 1 \
    --ClusterType 2 \
    --ClusterId cluster-5c42n3a5 \
    --WorkSpaceId space-53rqk422 \
    --Description some description
```

Output: 
```
{
    "Response": {
        "JobId": "cql-e92rhppb",
        "RequestId": "9159e720-d61c-459f-862b-d630de3209dd"
    }
}
```

