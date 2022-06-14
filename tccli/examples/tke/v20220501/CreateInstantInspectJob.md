**Example 1: 获得集群巡检结果**



Input: 

```
tccli tke CreateInstantInspectJob --cli-unfold-argument  \
    --MatchLabels.0.Name AppId \
    --MatchLabels.0.Value 123456
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "JobName": "job-test"
    }
}
```

