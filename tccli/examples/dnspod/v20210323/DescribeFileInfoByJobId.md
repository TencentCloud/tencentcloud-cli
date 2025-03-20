**Example 1: 获取文件信息**

根据任务ID获取文件信息

Input: 

```
tccli dnspod DescribeFileInfoByJobId --cli-unfold-argument  \
    --JobId 1808638
```

Output: 
```
{
    "Response": {
        "FileInfo": {
            "CreatedOn": "2025-03-07 15:04:47",
            "Domains": [
                "dnspod.cn"
            ],
            "FileId": 1620903,
            "FileUrl": null,
            "JobId": 1808638,
            "LeftTime": {
                "Days": 0,
                "Hours": 0,
                "Mins": 0
            },
            "Name": "dnspod_statistics_dnspod.cn_2025-03-01-2025-03-07.xlsx",
            "Progress": 0,
            "Status": "canceled",
            "Type": "record_log",
            "UpdatedOn": "2025-03-07 15:06:32"
        },
        "RequestId": "aeb64ecb-b69c-4c09-9c59-c2e52ae8a48e"
    }
}
```

