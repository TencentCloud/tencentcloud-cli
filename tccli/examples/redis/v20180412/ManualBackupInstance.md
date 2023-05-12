**Example 1: 请求示例**

手动备份

Input: 

```
tccli redis ManualBackupInstance --cli-unfold-argument  \
    --InstanceId crs-5a4p**** \
    --Remark xxxx
```

Output: 
```
{
    "Response": {
        "TaskId": "6954227",
        "RequestId": "4daddc97-0005-45d8-b5b8-38514ec1e97c"
    }
}
```

