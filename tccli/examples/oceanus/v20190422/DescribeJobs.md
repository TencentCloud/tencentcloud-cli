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
                "TotalRunMillis": 2264500,
                "Zone": "xx",
                "Remark": "xx",
                "FlinkVersion": "xx",
                "WebUIUrl": "xx",
                "Name": "xx",
                "Status": 4,
                "UpdateTime": "xx",
                "CreatorUin": "xx",
                "WorkSpaceName": "xx",
                "RunningCu": 0.0,
                "ClusterId": "xx",
                "JobId": "xx",
                "WorkSpaceId": "xx",
                "LastOpResult": "xx",
                "RunningCuNum": 1,
                "SchedulerType": 1,
                "JobType": 1,
                "CuMem": 4,
                "LatestJobConfigVersion": 2,
                "Region": "xx",
                "OwnerUin": "xx",
                "StopTime": "xx",
                "PublishedJobConfigVersion": 2,
                "StatusDesc": "xx",
                "ClusterName": "xx",
                "StartTime": "xx",
                "AppId": 1234567890,
                "ClusterStatus": 0,
                "CurrentRunMillis": 3201,
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

