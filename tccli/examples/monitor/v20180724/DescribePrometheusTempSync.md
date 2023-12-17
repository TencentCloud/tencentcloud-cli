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
                "Region": "abc",
                "InstanceId": "abc",
                "ClusterId": "abc",
                "SyncTime": "abc",
                "Version": "abc",
                "ClusterType": "abc",
                "InstanceName": "abc",
                "ClusterName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

