**Example 1: 获取集群资源使用量**



Input: 

```
tccli tke DescribeResourceUsage --cli-unfold-argument  \
    --ClusterId xx
```

Output: 
```
{
    "Response": {
        "CRDUsage": {
            "Details": [
                {
                    "Name": "tkeserviceconfigs",
                    "Usage": 0
                }
            ],
            "Name": "CRD",
            "Usage": 0
        },
        "ConfigMapUsage": 14,
        "OtherUsage": {
            "Details": [
                {
                    "Name": "clusterrolebindings",
                    "Usage": 47
                },
                {
                    "Name": "endpoints",
                    "Usage": 4
                }
            ],
            "Name": "Other",
            "Usage": 51
        },
        "PodUsage": 3,
        "RequestId": "c7ad171e-3604-4662-b3b8-cd10b818a407"
    }
}
```

