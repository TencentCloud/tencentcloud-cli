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
        "Data": "V1",
        "RequestId": "ba2f7cf1-f2ff-4cd2-9951-312f924c5ef4"
    }
}
```

