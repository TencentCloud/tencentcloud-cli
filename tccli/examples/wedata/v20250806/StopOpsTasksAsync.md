**Example 1: 任务下线**

运维中心-任务运维-任务下线

Input: 

```
tccli wedata StopOpsTasksAsync --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskIds 20250630162948606
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncId": "0e719593-65b7-4616-b217-44461e37414e"
        },
        "RequestId": "7b6d888e-cdfa-4478-bcf9-1e48579b62f2"
    }
}
```

