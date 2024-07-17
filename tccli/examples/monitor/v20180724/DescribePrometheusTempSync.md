**Example 1: 拉取同步目标**

拉取同步目标

Input: 

```
tccli monitor DescribePrometheusTempSync --cli-unfold-argument  \
    --TemplateId "temp-xxx"
```

Output: 
```
{
    "Response": {
        "Targets": [
            {
                "Region": "ap-beijing",
                "InstanceId": "prom-sjfgh",
                "ClusterId": "cls-kdje",
                "SyncTime": "2024-07-16 16:28:54",
                "Version": "v1",
                "ClusterType": "tke",
                "InstanceName": "test-prom",
                "ClusterName": "test-cluster"
            }
        ],
        "RequestId": "abc"
    }
}
```

