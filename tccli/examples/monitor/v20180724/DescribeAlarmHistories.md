**Example 1: 查询告警历史**



Input: 

```
tccli monitor DescribeAlarmHistories --cli-unfold-argument  \
    --Module monitor \
    --PageNumber 1 \
    --PageSize 10 \
    --StartTime 1598976507 \
    --EndTime 1599019707
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Histories": [
            {
                "AlarmId": "abc",
                "MonitorType": "abc",
                "Namespace": "abc",
                "AlarmObject": "abc",
                "Content": "abc",
                "FirstOccurTime": 0,
                "LastOccurTime": 0,
                "AlarmStatus": "abc",
                "PolicyId": "abc",
                "PolicyName": "abc",
                "VPC": "abc",
                "ProjectId": 0,
                "ProjectName": "abc",
                "InstanceGroup": [
                    {
                        "Id": 0,
                        "Name": "abc"
                    }
                ],
                "ReceiverUids": [
                    0
                ],
                "ReceiverGroups": [
                    0
                ],
                "NoticeWays": [
                    "abc"
                ],
                "OriginId": "abc",
                "AlarmType": "abc",
                "EventId": 0,
                "Region": "abc",
                "PolicyExists": 0,
                "MetricsInfo": [
                    {
                        "QceNamespace": "abc",
                        "MetricName": "abc",
                        "Period": 0,
                        "Value": "abc",
                        "Description": "abc"
                    }
                ],
                "Dimensions": "abc",
                "AlarmLevel": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 查询“云服务器-基础监控”的告警历史**

监控类型是一级概念，策略类型是二级概念，因此在 Namespaces 字段中只有在指定监控类型后，策略类型才有意义。

如果要查询“云服务器-基础监控”的告警历史，这里的过滤条件应为：监控类型=“云产品监控”，策略类型=“云服务器-基础监控”

MonitorTypes 作为一级过滤条件应填入 `["MT_QCE"]`

Namespaces 作为二级过滤条件应填入 `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`

Input: 

```
tccli monitor DescribeAlarmHistories --cli-unfold-argument  \
    --Module monitor \
    --PageNumber 1 \
    --PageSize 10 \
    --StartTime 1598976507 \
    --EndTime 1599019707 \
    --MonitorTypes MT_QCE \
    --Namespaces.0.MonitorType MT_QCE \
    --Namespaces.0.Namespace cvm_device
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Histories": [
            {
                "AlarmId": "abc",
                "MonitorType": "abc",
                "Namespace": "abc",
                "AlarmObject": "abc",
                "Content": "abc",
                "FirstOccurTime": 0,
                "LastOccurTime": 0,
                "AlarmStatus": "abc",
                "PolicyId": "abc",
                "PolicyName": "abc",
                "VPC": "abc",
                "ProjectId": 0,
                "ProjectName": "abc",
                "InstanceGroup": [
                    {
                        "Id": 0,
                        "Name": "abc"
                    }
                ],
                "ReceiverUids": [
                    0
                ],
                "ReceiverGroups": [
                    0
                ],
                "NoticeWays": [
                    "abc"
                ],
                "OriginId": "abc",
                "AlarmType": "abc",
                "EventId": 0,
                "Region": "abc",
                "PolicyExists": 0,
                "MetricsInfo": [
                    {
                        "QceNamespace": "abc",
                        "MetricName": "abc",
                        "Period": 0,
                        "Value": "abc",
                        "Description": "abc"
                    }
                ],
                "Dimensions": "abc",
                "AlarmLevel": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

