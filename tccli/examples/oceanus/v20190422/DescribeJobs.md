**Example 1: 查询作业列表**



Input: 

```
tccli oceanus DescribeJobs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "JobSet": [
            {
                "AppId": 1234567890,
                "ClusterId": "cluster-c89m6luu",
                "ClusterName": "--",
                "CreateTime": "2019-11-01 22:31:55",
                "CreatorUin": "100006381234",
                "CuMem": 4,
                "CurrentRunMillis": 3201,
                "JobId": "cql-jb4du0gf",
                "JobType": 1,
                "LastOpResult": "",
                "LatestJobConfigVersion": 2,
                "Name": "sql-test",
                "OwnerUin": "100006381234",
                "PublishedJobConfigVersion": 2,
                "Region": "ap-shanghai",
                "Remark": "",
                "RunningCuNum": 1,
                "StartTime": "2019-11-02 11:34:55",
                "Status": 4,
                "StatusDesc": "running",
                "StopTime": "-",
                "TotalRunMillis": 2264500,
                "UpdateTime": "2019-11-02 11:34:55",
                "Zone": "ap-shanghai-3",
                "WebUIUrl": "xx",
                "SchedulerType": 1
            }
        ],
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccca348a"
    }
}
```

