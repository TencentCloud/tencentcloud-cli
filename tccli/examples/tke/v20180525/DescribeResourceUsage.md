**Example 1: 获取集群资源使用量**

描述集群资源使用量

Input: 

```
tccli tke DescribeResourceUsage --cli-unfold-argument  \
    --ClusterId cls-9jqo5g3a
```

Output: 
```
{
    "Response": {
        "CRDUsage": {
            "Name": "CRD",
            "Usage": 0,
            "Details": [
                {
                    "Name": "tkeserviceconfigs",
                    "Usage": 0
                }
            ]
        },
        "PodUsage": 3,
        "RSUsage": 3,
        "ConfigMapUsage": 14,
        "OtherUsage": {
            "Name": "Other",
            "Usage": 51,
            "Details": [
                {
                    "Name": "clusterrolebindings",
                    "Usage": 47
                },
                {
                    "Name": "endpoints",
                    "Usage": 4
                }
            ]
        },
        "RequestId": "c7ad171e-3604-4662-b3b8-cd10b818a407"
    }
}
```

