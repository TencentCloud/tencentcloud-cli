**Example 1: 请求健康得分**



Input: 

```
tccli dbbrain DescribeHealthScore --cli-unfold-argument  \
    --InstanceId cdb-8jawylhf \
    --Product mysql \
    --Time 2021-02-01T14:30:00+00:00
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

