**Example 1: 获得集群巡检结果**



Input: 

```
tccli tke DescribeInstantInspectTask --cli-unfold-argument  \
    --JobName job-test
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Status": "waiting",
        "Data": []
    }
}
```

