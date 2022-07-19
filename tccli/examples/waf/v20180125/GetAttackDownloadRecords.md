**Example 1: 查询下载攻击日志任务记录列表**



Input: 

```
tccli waf GetAttackDownloadRecords --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Id": 100003,
                "TaskName": "20201027-fuqian",
                "TaskId": "a5b05859-54d5-4cb2-b1af-c19b5195758b",
                "Host": "all",
                "CreateTime": "2020-10-28 00:36:19",
                "ModifyTime": "2020-10-28 01:04:15",
                "ExpireTime": "2020-11-04 00:36:19",
                "Count": 752507,
                "TotalCount": 752507,
                "Status": 1,
                "Url": "https://log-1256704386.cos.ap-guangzhou.myqcloud.com/cls/a5b05859-54d5-4cb2-b1af-c19b5195758b.zip"
            },
            {
                "Id": 100004,
                "TaskName": "20201027-fuqian",
                "TaskId": "6d68a0a5-c646-4b7a-ba95-f36b79f2921d",
                "Host": "all",
                "CreateTime": "2020-10-28 10:55:07",
                "ModifyTime": "2020-10-28 10:58:47",
                "ExpireTime": "2020-11-04 10:55:07",
                "Count": 150000,
                "TotalCount": 150000,
                "Status": 4,
                "Url": ""
            }
        ],
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

