**Example 1: 异步重跑自身实例**

仅重跑自己

Input: 

```
tccli wedata RerunTaskInstancesAsync --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --InstanceKeyList '20250714200130106_2025-10-01 00:00:00'
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncId": "14f05312-e8d6-4b7e-9221-ddc2be422780"
        },
        "RequestId": "089f0c66-232c-4fee-9993-aa3bb32036dd"
    }
}
```

