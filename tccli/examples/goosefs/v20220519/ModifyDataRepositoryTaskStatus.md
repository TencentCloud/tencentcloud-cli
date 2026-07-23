**Example 1: 暂停调用**



Input: 

```
tccli goosefs ModifyDataRepositoryTaskStatus --cli-unfold-argument  \
    --FileSystemId x-c60-3980hscb \
    --TaskId x_task_1782961196561 \
    --ModifyType pause
```

Output: 
```
{
    "Response": {
        "RequestId": "6e318cc3-776d-43fb-9cf2-617792c528c0"
    }
}
```

