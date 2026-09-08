**Example 1: 查询接入任务失败详情**



Input: 

```
tccli cls DescribeResourceGraphIngestTaskFailureDetail --cli-unfold-argument  \
    --ResourceGraphId 92005fca-cbf5-45e9-8c55-a506d8ff7238 \
    --TaskId e7a31fbb-1182-45ad-b756-cbb6597696a5
```

Output: 
```
{
    "Response": {
        "ErrorMessage": "TKE provision failed: ensure log-agent: tke-log-agent deployed version \"0.0.5\" is lower than base version \"2.0.8\" on cluster cls-dhf2fygk",
        "FirstFailedAt": 0,
        "LastFailedTime": 1785323250,
        "Operation": "create",
        "RetryCount": 0,
        "RequestId": "d757456e-c430-4b24-b756-003fe4982ac3"
    }
}
```

