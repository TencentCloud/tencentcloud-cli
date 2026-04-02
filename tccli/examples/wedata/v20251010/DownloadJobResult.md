**Example 1: 获取任务结果**



Input: 

```
tccli wedata DownloadJobResult --cli-unfold-argument  \
    --WorkspaceId 12345677 \
    --JobId 12 \
    --SubJobId 12 \
    --RequestType None
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadUrls": [
                "https://log-detail.example.com/jobs/12/logs"
            ],
            "ResultMeta": {
                "CostTime": 123,
                "CreateTime": "1764819834754",
                "ResultSchema": [
                    {
                        "Name": "id",
                        "Type": "int"
                    }
                ],
                "SQL": "/tmp/job_logs/12/default_output.log"
            }
        },
        "RequestId": "f034a107-5055-4517-8acd-320e13232629"
    }
}
```

