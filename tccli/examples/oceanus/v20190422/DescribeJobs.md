**Example 1: demo**



Input: 

```
tccli oceanus DescribeJobs --cli-unfold-argument  \
    --JobIds cql-c02rgjsj
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "JobId": "cql-c02rgjsj",
                "Region": "ap-chongqing",
                "Zone": "ap-chongqing-1",
                "AppId": 1257052345,
                "OwnerUin": "1002342346",
                "CreatorUin": "1000372342342",
                "Name": "paimon120test",
                "JobType": 1,
                "ClusterName": "rwr0707",
                "RunningCuNum": 2,
                "RunningCu": 2,
                "CuMem": 4,
                "LatestJobConfigVersion": 1,
                "LatestValidJobConfigVersion": 1,
                "PublishedJobConfigVersion": 1,
                "Status": 4,
                "StatusDesc": "running",
                "CreateTime": "2026-07-30 16:26:29",
                "StartTime": "2026-07-30 16:29:44",
                "StopTime": "2026-07-30 16:30:06",
                "UpdateTime": "2026-07-30 16:30:06",
                "CurrentRunMillis": 424807099,
                "TotalRunMillis": 424807099,
                "Remark": "",
                "Description": "",
                "LastOpResult": "",
                "ClusterId": "cluster-sdfsa",
                "WebUIUrl": "https://ap-chongqing.flinkui.qcloudoceanus.com/cluster-sdfsa/cql-c02rgjsj-837534/?defaultToken=0",
                "SchedulerType": 2,
                "ClusterStatus": 2,
                "FlinkVersion": "Flink-1.20",
                "JdkVersion": "8",
                "WorkSpaceId": "space-dzsdfn3",
                "WorkSpaceName": "Default",
                "Tags": null,
                "EventInfo": {
                    "ErrorEventTotal": 0
                }
            }
        ],
        "RequestId": "e27d0353-bsdfs7-496c-b13f-1b241d935d6f",
        "TotalCount": 31
    }
}
```

