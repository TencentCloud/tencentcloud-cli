**Example 1: 获取健康得分**

通过实例ID获取健康得分，以及异常扣分项。

Input: 

```
tccli dbbrain DescribeHealthScore --cli-unfold-argument  \
    --InstanceId test \
    --Time 2019-01-01T00:00:00+08:00 \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "RequestId": "8b307450-6118-11eb-88ad-93c053da68c6",
        "Data": {
            "IssueTypes": [
                {
                    "TotalCount": 0,
                    "Events": [],
                    "IssueType": "AVAILABILITY"
                },
                {
                    "TotalCount": 0,
                    "Events": [],
                    "IssueType": "MAINTAINABILITY"
                },
                {
                    "TotalCount": 1,
                    "Events": [
                        {
                            "DiagType": "高并发/压力请求",
                            "ScoreLost": 6,
                            "StartTime": "2020-09-22T00:00:00+00:00",
                            "EndTime": "2020-09-22T00:00:00+00:00",
                            "EventId": 780019530,
                            "Outline": "监控指标 \"cpu_use_rate\" 告警，当前值 100",
                            "Severity": 1,
                            "Metric": "cpu_use_rate",
                            "Count": 1
                        }
                    ],
                    "IssueType": "PERFORMANCE"
                },
                {
                    "TotalCount": 3,
                    "Events": [
                        {
                            "DiagType": "复制",
                            "ScoreLost": 10,
                            "StartTime": "2020-09-22T00:00:00+00:00",
                            "EndTime": "2020-09-22T00:00:00+00:00",
                            "EventId": 780018741,
                            "Outline": "复制IO线程中断",
                            "Severity": 1,
                            "Metric": "slave_io_running",
                            "Count": 1
                        },
                        {
                            "DiagType": "复制",
                            "ScoreLost": 10,
                            "StartTime": "2020-09-22T00:00:00+00:00",
                            "EndTime": "2020-09-22T00:00:00+00:00",
                            "EventId": 779984938,
                            "Outline": "复制IO线程中断",
                            "Severity": 1,
                            "Metric": "slave_io_running",
                            "Count": 1
                        },
                        {
                            "DiagType": "复制",
                            "ScoreLost": 8,
                            "StartTime": "2020-09-22T00:00:00+00:00",
                            "EndTime": "2020-09-22T00:00:00+00:00",
                            "EventId": 780021648,
                            "Outline": "复制延迟",
                            "Severity": 2,
                            "Metric": "slave_io_running",
                            "Count": 1
                        }
                    ],
                    "IssueType": "RELIABILITY"
                }
            ],
            "EventsTotalCount": 4,
            "HealthLevel": "RISK"
        }
    }
}
```

**Example 2: 请求健康得分**

请求健康得分。

Input: 

```
tccli dbbrain DescribeHealthScore --cli-unfold-argument  \
    --InstanceId cdb-8jawylhf \
    --Product mysql \
    --Time 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "0736b315-a9be-4991-92e6-28eccf3d31e3",
        "Data": {
            "IssueTypes": [
                {
                    "TotalCount": 0,
                    "Events": [],
                    "IssueType": "AVAILABILITY"
                },
                {
                    "TotalCount": 0,
                    "Events": [],
                    "IssueType": "MAINTAINABILITY"
                },
                {
                    "TotalCount": 0,
                    "Events": [],
                    "IssueType": "PERFORMANCE"
                },
                {
                    "TotalCount": 0,
                    "Events": [],
                    "IssueType": "RELIABILITY"
                }
            ],
            "HealthScore": 100,
            "EventsTotalCount": 0,
            "HealthLevel": "HEALTH"
        }
    }
}
```

