**Example 1: 查询任务结果**

查询ES产品某集群实例指定时间段护航结果

Input: 

```
tccli qinge QueryTcoTaskResult --cli-unfold-argument  \
    --Condition es-3owp63sp \
    --StartTime 1715796900 \
    --EndTime 1715797560 \
    --TaskType INSPECT_ES
```

Output: 
```
{
    "Response": {
        "CodeMsg": {
            "Message": "Succ",
            "Retcode": 0
        },
        "RequestId": "1691632520065",
        "TaskResults": [
            {
                "Switch": 0,
                "Desc": "存在集群规格为 1C2G/2C2G 的集群。集群内存过低，容易出现因 oom 导致节点宕机的情况。1C2G/2C2G 集群严禁用于生产环境。",
                "Scope": "影响范围",
                "Suggestion": "长期解决方案：建议升级集群规格，至少为2C4G。",
                "Id": 4043423,
                "TaskKey": "1fe4f2cf-b86b-4168-8408-b891807f3a78",
                "ExceptionNum": 1,
                "InspectionType": "metric",
                "InstanceId": "es-3owp63sp",
                "Ip": "",
                "Service": "ES",
                "Role": "ESMetrics",
                "Type": "MemorySpecification1C2G_ESInstanceMemorySpecification",
                "Name": "内存规格1C2G巡检",
                "Message": "9.15.64.250(1C2G)",
                "Notify": 6,
                "CreateTime": "2024-05-16T02:25:02+08:00",
                "AppId": 1259242701,
                "Uin": "100010224120",
                "Threshold": "2",
                "ThresholdOperator": "-",
                "AppIdStr": "1259242701",
                "DbId": 2336,
                "RegionId": 8,
                "RegionName": "华北地区(北京)",
                "StartTime": 1715186400,
                "EndTime": 1715791200,
                "Level": 0,
                "ParentTaskKey": "1fe4f2cf-b86b-4168-8408-b891807f3a78",
                "MessageAll": "Id:ins-2bp5vgq3,Ip:9.15.64.250,异常值:1C2G"
            },
            {
                "Switch": 0,
                "Desc": "",
                "Scope": "",
                "Suggestion": "",
                "Id": 4043397,
                "TaskKey": "1fe4f2cf-b86b-4168-8408-b891807f3a78",
                "ExceptionNum": 1,
                "InspectionType": "metric",
                "InstanceId": "es-3owp63sp",
                "Ip": "",
                "Service": "ES",
                "Role": "ESMetrics",
                "Type": "InstanceLatestVersion_ESLatestVersion",
                "Name": "集群非最新版本",
                "Message": "kernelVersion:, version:71001.20211224.xpack612b9603",
                "Notify": 6,
                "CreateTime": "2024-05-16T02:25:01+08:00",
                "AppId": 1259242701,
                "Uin": "100010224120",
                "Threshold": "-",
                "ThresholdOperator": "-",
                "AppIdStr": "1259242701",
                "DbId": 2336,
                "RegionId": 8,
                "RegionName": "华北地区(北京)",
                "StartTime": 1715186400,
                "EndTime": 1715791200,
                "Level": 0,
                "ParentTaskKey": "1fe4f2cf-b86b-4168-8408-b891807f3a78",
                "MessageAll": "ClusterId:es-3owp63sp, kernelVersion:, Version:71001.20211224.xpack612b9603"
            }
        ],
        "TotalCount": 2
    }
}
```

