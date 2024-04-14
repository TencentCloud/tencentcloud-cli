**Example 1: 1**

2

Input: 

```
tccli wedata CommitIntegrationTask --cli-unfold-argument  \
    --TaskId kb947c997-4f91-4a1f-913d-06f66a5fb927 \
    --ProjectId 1486804694126882816 \
    --CommitType 1 \
    --TaskType 201 \
    --VersionDesc v1 \
    --InstanceVersion 3
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnsupportedOperation",
            "Message": "CloudApiException: The current task is locked by 100028625403 and cannot be committed"
        },
        "RequestId": "6a160ebb-720b-47a7-8f88-4e30f033955d"
    }
}
```

**Example 2: 提交集成任务**

提交集成任务

Input: 

```
tccli wedata CommitIntegrationTask --cli-unfold-argument  \
    --TaskId 3cd6b1b3-76a0-4147-8f0e-6df206bc58c0 \
    --ProjectId 1 \
    --CommitType 0 \
    --TaskType 1 \
    --ExtConfig.0.Name name1 \
    --ExtConfig.0.Value 1
```

Output: 
```
{
    "Response": {
        "RequestId": "as1cs2c123asyi23bh213cc",
        "Data": true
    }
}
```

