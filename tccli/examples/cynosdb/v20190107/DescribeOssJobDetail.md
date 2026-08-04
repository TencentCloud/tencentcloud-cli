**Example 1: 查询管控jobid**



Input: 

```
tccli cynosdb DescribeOssJobDetail --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qjtwvlxa \
    --JobId 18290681
```

Output: 
```
{
    "Response": {
        "Author": "700001815885",
        "CreateTime": "2026-05-18 15:42:04",
        "EndTime": "2026-05-18 15:42:26",
        "ErrNo": 0,
        "ErrorMessage": "",
        "JobId": "18290681",
        "JobType": "set_pfs_status",
        "Message": "",
        "MessageCode": 0,
        "Progress": 100,
        "Status": 0,
        "RequestId": "ce0b0f75-38d9-43fa-b579-258acfc83a19"
    }
}
```

