**Example 1: 查询审计日志文件列表**

查询审计日志文件列表

Input: 

```
tccli dbbrain DescribeAuditLogFiles --cli-unfold-argument  \
    --Product dcdb \
    --NodeRequestType dcdb \
    --InstanceId tdsql-cerses
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "8ca4d610-dcf3-11ed-9a8b-393823b6fd49",
        "Items": [
            {
                "Status": "success",
                "AsyncRequestId": 173,
                "ErrMsg": "",
                "CreateTime": "2023-04-17 15:37:55",
                "FileName": "tdsql-8fyt6dkd_20230417-151100_to_20230417-151403_1681717077964.tar.gz",
                "FileSize": 0.326,
                "DownloadUrl": "https://dbbrain-gz-xxx.cos.ap-guangzhou.tencentcos.cn/tdsql-8fyt6dkd_20230417-151100_to_20230417-151403_1681717077964.tar.gz?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDkMfJhxjhBTahcIaNgNsBKDwZx74pmsY3%2638be613391610",
                "Progress": 22,
                "FinishTime": "2024-07-23 16:05:23"
            }
        ]
    }
}
```

