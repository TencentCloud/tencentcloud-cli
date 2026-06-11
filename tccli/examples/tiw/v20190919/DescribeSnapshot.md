**Example 1: 查询白板快照任务**

查询白板快照任务

Input: 

```
tccli tiw DescribeSnapshot --cli-unfold-argument  \
    --TaskId g0jb42ps49vtebjshilb \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "Snapshots": [
            "https://snapshot-result-1400000001.example.com/snapshot/0dhhmtptvchupgqo0q0d/1747905311610.mrk",
            "https://snapshot-result-1400000001.example.com/snapshot/0dhhmtptvchupgqo0q0d/1747905282346.mrk"
        ],
        "Status": "FINISHED",
        "TaskId": "0dhhmtptvchupgqo0q0d"
    }
}
```

