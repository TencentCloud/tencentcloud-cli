**Example 1: GC 最近10条历史**



Input: 

```
tccli tcr DescribeGCJobs --cli-unfold-argument  \
    --RegistryId tcr-test123
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "UpdateTime": "2021-06-01T08:10:42.713895Z",
                "CreationTime": "2021-06-01T08:10:42Z",
                "ID": 65,
                "JobStatus": "pending"
            },
            {
                "UpdateTime": "2021-05-28T09:01:36.772412Z",
                "CreationTime": "2021-05-28T09:01:36Z",
                "ID": 56,
                "JobStatus": "finished"
            }
        ],
        "RequestId": "c3fca04b-76c4-4165-8fad-824ce73dd0f8"
    }
}
```

