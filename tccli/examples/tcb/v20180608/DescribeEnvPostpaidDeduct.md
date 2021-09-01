**Example 1: 查询环境后付费计费详情**

查询环境后付费计费详情

Input: 

```
tccli tcb DescribeEnvPostpaidDeduct --cli-unfold-argument  \
    --EnvId cdnheader-v2a \
    --StartTime 2021-09-09 \
    --EndTime 2021-09-09 \
    --ResourceTypes COS
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351",
        "PostPaidEnvDeductInfoList": [
            {
                "EnvId": "nanatest-6gh4z1im209cc32c",
                "FreeQuota": 0.0017,
                "MetricName": "ReadRequests",
                "PkgQuota": 0,
                "ResQuota": 0,
                "ResourceType": "COS"
            },
            {
                "EnvId": "nanatest-6gh4z1im209cc32c",
                "FreeQuota": 0.0001,
                "MetricName": "WriteRequests",
                "PkgQuota": 0,
                "ResQuota": 0,
                "ResourceType": "COS"
            }
        ]
    }
}
```

