**Example 1: 异步暂停任务**

运维中心-任务运维-暂停任务

Input: 

```
tccli wedata PauseOpsTasksAsync --cli-unfold-argument  \
    --ProjectId 2763518183736183934 \
    --TaskIds 20250630162948606
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncId": "b8e6abb4-d99f-4ef3-9580-edcce7676a82"
        },
        "RequestId": "3259454a-bdd9-4152-a749-7e88c4725ff5"
    }
}
```

