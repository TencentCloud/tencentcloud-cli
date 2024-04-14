**Example 1: batchstop**

测试环境实际停止用例

Input: 

```
tccli wedata BatchStopIntegrationTasks --cli-unfold-argument  \
    --TaskIds l9c13c798-6488-4de6-971e-21796f797929 \
    --TaskType 201 \
    --ProjectId 1486804694126882816
```

Output: 
```
{
    "Response": {
        "FailedCount": 0,
        "RequestId": "fc4e5ff1-262e-43f9-aa09-5b5543905423",
        "SuccessCount": 1,
        "TaskNames": [
            "l9c13c798-6488-4de6-971e-21796f797929"
        ],
        "TotalCount": 1
    }
}
```

**Example 2: BatchStopIntegrationTasks**



Input: 

```
tccli wedata BatchStopIntegrationTasks --cli-unfold-argument  \
    --TaskIds 20220506145218687 \
    --TaskType 0 \
    --ProjectId 11022568003970304
```

Output: 
```
{
    "Response": {
        "SuccessCount": 0,
        "FailedCount": 0,
        "TotalCount": 0,
        "TaskNames": [
            "20220506145218687"
        ],
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

