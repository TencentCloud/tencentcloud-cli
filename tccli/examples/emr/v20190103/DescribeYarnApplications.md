**Example 1: 获取Yarn的Applications列表**

获取Yarn的Applications列表

Input: 

```
tccli emr DescribeYarnApplications --cli-unfold-argument  \
    --InstanceId emr-qy2p6mem \
    --Offset 0 \
    --Limit 2 \
    --StartTime 1685633400 \
    --EndTime 1686239999
```

Output: 
```
{
    "Response": {
        "Total": 225,
        "RequestId": "12345678999",
        "Results": [
            {
                "MemorySeconds": 5512381,
                "NumAMContainerPreempted": 0,
                "HDFSBytesWritten": 0,
                "MapOutputRecords": 0,
                "State": "",
                "FailedReduceAttempts": 0,
                "ApplicationType": "TEZ",
                "MbMillisMaps": 0,
                "Progress": 0,
                "GcTimeMillis": 0,
                "ReducesCompleted": 0,
                "MapInputRecords": 0,
                "KilledMapAttempts": 0,
                "RunningContainers": 0,
                "ReduceOutputRecords": 0,
                "TotalLaunchedMaps": 0,
                "VCoreSeconds": 3175,
                "AllocatedMB": 0,
                "AvgReduceTime": 0,
                "ClusterUsagePercentage": 0,
                "User": "hadoop",
                "PreemptedResourceMB": 0,
                "FinishedTime": -1,
                "TotalLaunchedReduces": 0,
                "Name": "HIVE-a4ee6338-7b65-4e10-a5fe-717ff8f5c1a7",
                "AvgShuffleTime": 0,
                "ReducesTotal": 0,
                "PreemptedResourceVCores": 0,
                "StartedTime": 1686156754000,
                "ElapsedTime": "12min14s",
                "MbMillisReduces": 0,
                "NumNonAMContainerPreempted": 0,
                "MapsCompleted": 0,
                "ReduceInputRecords": 0,
                "KilledReduceAttempts": 0,
                "FailedMapAttempts": 0,
                "SuccessfulReduceAttempts": 0,
                "Queue": "default",
                "VCoreMillisMaps": 0,
                "AvgMapTime": 0,
                "AllocatedVCores": 0,
                "HDFSBytesRead": 0,
                "VCoreMillisReduces": 0,
                "MapsTotal": 0,
                "FinalStatus": "UNDEFINED",
                "AvgMergeTime": 0,
                "Id": "application_1686105960659_0022",
                "QueueUsagePercentage": 0,
                "SuccessfulMapAttempts": 0
            },
            {
                "MemorySeconds": 4415161,
                "NumAMContainerPreempted": 0,
                "HDFSBytesWritten": 0,
                "MapOutputRecords": 0,
                "State": "",
                "FailedReduceAttempts": 0,
                "ApplicationType": "TEZ",
                "MbMillisMaps": 0,
                "Progress": 0,
                "GcTimeMillis": 0,
                "ReducesCompleted": 0,
                "MapInputRecords": 0,
                "KilledMapAttempts": 0,
                "RunningContainers": 0,
                "ReduceOutputRecords": 0,
                "TotalLaunchedMaps": 0,
                "VCoreSeconds": 2934,
                "AllocatedMB": 0,
                "AvgReduceTime": 0,
                "ClusterUsagePercentage": 0,
                "User": "hadoop",
                "PreemptedResourceMB": 0,
                "FinishedTime": -1,
                "TotalLaunchedReduces": 0,
                "Name": "HIVE-113e63ac-47f4-449f-b690-fa52358f348b",
                "AvgShuffleTime": 0,
                "ReducesTotal": 0,
                "PreemptedResourceVCores": 0,
                "StartedTime": 1686152517000,
                "ElapsedTime": "7min38s",
                "MbMillisReduces": 0,
                "NumNonAMContainerPreempted": 0,
                "MapsCompleted": 0,
                "ReduceInputRecords": 0,
                "KilledReduceAttempts": 0,
                "FailedMapAttempts": 0,
                "SuccessfulReduceAttempts": 0,
                "Queue": "default",
                "VCoreMillisMaps": 0,
                "AvgMapTime": 0,
                "AllocatedVCores": 0,
                "HDFSBytesRead": 0,
                "VCoreMillisReduces": 0,
                "MapsTotal": 0,
                "FinalStatus": "UNDEFINED",
                "AvgMergeTime": 0,
                "Id": "application_1686105960659_0021",
                "QueueUsagePercentage": 0,
                "SuccessfulMapAttempts": 0
            }
        ]
    }
}
```

