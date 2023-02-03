**Example 1: 创建上传文件系统数据到存储桶任务**

创建上传文件系统数据到存储桶任务

Input: 

```
tccli goosefs CreateDataRepositoryTask --cli-unfold-argument  \
    --TaskName my_test_task \
    --FileSystemId x_c60_r3c4fa1f \
    --Bucket mybucket-1250000 \
    --TaskPath aaa/bbb \
    --TaskType FS_TO_BUCKET \
    --RepositoryType MSP_AFM
```

Output: 
```
{
    "Response": {
        "TaskId": "c1a2b3f4",
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

