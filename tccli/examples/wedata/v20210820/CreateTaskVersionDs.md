**Example 1: 失败**

失败

Input: 

```
tccli wedata CreateTaskVersionDs --cli-unfold-argument  \
    --Task.TaskId 20230516193558842 \
    --Task.VersionRemark version_1 \
    --NeedCheckParentSubmitted False \
    --AutoRun False \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "操作失败"
        },
        "RequestId": "ba2f7cf1-f2ff-4cd2-9951-312f924c5ef4"
    }
}
```

**Example 2: 成功**

成功

Input: 

```
tccli wedata CreateTaskVersionDs --cli-unfold-argument  \
    --Task.TaskId 20250808113834792 \
    --Task.VersionRemark py_task \
    --Task.FolderId 3a80fd12-4b82-11f0-8ec8-b8599f277de5 \
    --NeedCheckParentSubmitted True \
    --AutoRun True \
    --ProjectId 1470547050521227264 \
    --RequestFromSource WEB \
    --AlarmWays email \
    --AlarmRecipientTypes 2 \
    --EnableCheckTaskCycleLink False
```

Output: 
```
{
    "Response": {
        "Data": "V3",
        "RequestId": "cb3a154e-faff-48ad-847a-5b6e9be02ba2"
    }
}
```

