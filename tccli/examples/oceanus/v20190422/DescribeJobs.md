**Example 1: 查询作业**

查询作业

Input: 

```
tccli oceanus DescribeJobs --cli-unfold-argument  \
    --Limit 1 \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "AppId": 1257048945,
                "ClusterId": "cluster-5c43n3a5",
                "ClusterName": "cluster-test",
                "ClusterStatus": 2,
                "CreateTime": "2023-11-20 15:19:57",
                "CreatorUin": "100032489761",
                "CuMem": 4,
                "CurrentRunMillis": 0,
                "FlinkVersion": "Flink-1.13",
                "JobId": "cql-e92rh2pb",
                "JobType": 1,
                "LastOpResult": "",
                "LatestJobConfigVersion": 0,
                "Name": "create_job_test",
                "OwnerUin": "100006376216",
                "PublishedJobConfigVersion": -1,
                "Region": "ap-guangzhou",
                "Remark": "",
                "RunningCu": 0,
                "RunningCuNum": 0,
                "SchedulerType": 2,
                "StartTime": "-",
                "Status": 1,
                "StatusDesc": "create",
                "StopTime": "-",
                "Tags": null,
                "TotalRunMillis": 0,
                "UpdateTime": "2023-11-20 15:19:57",
                "WebUIUrl": "",
                "WorkSpaceId": "space-53rek422",
                "WorkSpaceName": "name",
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "ac6a62a7-45f1-4066-963d-eabea0f2824d",
        "TotalCount": 5
    }
}
```

