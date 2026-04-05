**Example 1: 下载任务日志**



Input: 

```
tccli wedata DownloadJobLog --cli-unfold-argument  \
    --JobId 12 \
    --WorkspaceId 1234567890 \
    --SubJobId None
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadUrl": "https://log-detail.example.com/jobs/12/logs?offset=100&limit=100"
        },
        "RequestId": "265b2760-8beb-4923-9e7c-4dbbad2b7037"
    }
}
```

