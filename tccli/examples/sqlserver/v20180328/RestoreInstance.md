**Example 1: 根据备份集回档数据库**

根据备份集回档数据库

Input: 

```
tccli sqlserver RestoreInstance --cli-unfold-argument  \
    --InstanceId mssql-u81902ja \
    --BackupId 0 \
    --TargetInstanceId mssql-u8190212 \
    --RenameRestore.0.OldName test_db \
    --RenameRestore.0.NewName new_db \
    --GroupId 
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "RequestId": "tqKar0yjquorXdNkDzkAZ8lh1_JTWJq3"
    }
}
```

