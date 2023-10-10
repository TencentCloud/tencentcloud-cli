**Example 1: 导出主机快照备份列表**

导出主机快照备份列表

Input: 

```
tccli cwp ExportRansomDefenseBackupList --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --Order abc \
    --By abc \
    --Quuid abc
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "123123"
    }
}
```

