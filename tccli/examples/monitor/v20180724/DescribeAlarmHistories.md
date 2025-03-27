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
        "TotalCount": 10,
        "Histories": [
            {
                "AlarmId": "23456789-12ab-45cd-8ef0-123456789",
                "MonitorType": "cvm",
                "Namespace": "cvm_device",
                "AlarmObject": "ins-123456",
                "Content": "实例 ins-123456 CPU 使用率过高",
                "FirstOccurTime": 1672531200,
                "LastOccurTime": 1672534800,
                "AlarmStatus": "2",
                "PolicyId": "policy-123456",
                "PolicyName": "云服务器 CPU 使用率告警策略",
                "VPC": "vpc-123456",
                "ProjectId": 12345,
                "ProjectName": "项目 A",
                "InstanceGroup": [
                    {
                        "Id": 1,
                        "Name": "生产环境实例组"
                    }
                ],
                "ReceiverUids": [
                    1001,
                    1002
                ],
                "ReceiverGroups": [
                    2001
                ],
                "NoticeWays": [
                    "sms",
                    "email"
                ],
                "OriginId": "1234567890",
                "AlarmType": "metric_alarm",
                "EventId": 123456,
                "Region": "ap-guangzhou",
                "PolicyExists": 1,
                "MetricsInfo": [
                    {
                        "QceNamespace": "qce/cvm",
                        "MetricName": "cpu_utilization",
                        "Period": 60,
                        "Value": "80",
                        "Description": "云服务器 CPU 使用率指标"
                    }
                ],
                "Dimensions": "{\"InstanceId\":\"ins-123456\"}",
                "AlarmLevel": "high"
            }
        ],
        "RequestId": "1234567890abcdef"
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
        "TotalCount": 10,
        "Histories": [
            {
                "AlarmId": "23456789-12ab-45cd-8ef0-123456789",
                "MonitorType": "cvm",
                "Namespace": "cvm_device",
                "AlarmObject": "ins-123456",
                "Content": "实例 ins-123456 CPU 使用率过高",
                "FirstOccurTime": 1672531200,
                "LastOccurTime": 1672534800,
                "AlarmStatus": "2",
                "PolicyId": "policy-123456",
                "PolicyName": "云服务器 CPU 使用率告警策略",
                "VPC": "vpc-123456",
                "ProjectId": 12345,
                "ProjectName": "项目 A",
                "InstanceGroup": [
                    {
                        "Id": 1,
                        "Name": "生产环境实例组"
                    }
                ],
                "ReceiverUids": [
                    1001,
                    1002
                ],
                "ReceiverGroups": [
                    2001
                ],
                "NoticeWays": [
                    "sms",
                    "email"
                ],
                "OriginId": "1234567890",
                "AlarmType": "metric_alarm",
                "EventId": 123456,
                "Region": "ap-guangzhou",
                "PolicyExists": 1,
                "MetricsInfo": [
                    {
                        "QceNamespace": "qce/cvm",
                        "MetricName": "cpu_utilization",
                        "Period": 60,
                        "Value": "80",
                        "Description": "云服务器 CPU 使用率指标"
                    }
                ],
                "Dimensions": "{\"InstanceId\":\"ins-123456\"}",
                "AlarmLevel": "high"
            }
        ],
        "RequestId": "1234567890abcdef"
    }
}
```

