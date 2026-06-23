**Example 1: RayCluster集群信息**



Input: 

```
tccli emr DescribeDynamicInstanceList --cli-unfold-argument  \
    --InstanceId emr-gq14f5p8
```

Output: 
```
{
    "Response": {
        "DynamicInstanceList": [
            {
                "CreateTime": "2026-06-22 21:00:17",
                "DashboardUrl": "http://10.10.0.169/raycluster-777",
                "Namespace": "251233702-emr-gq14f5p8",
                "PodCount": 2,
                "RayClusterId": 20,
                "RayClusterName": "raycluster-777",
                "RedisCount": 0,
                "SubmitType": 1
            }
        ],
        "WebUIInfos": [
            {
                "ServiceName": "JUPYTERLAB",
                "Url": "http://10.0.254.11:53487",
                "WebUIStatus": 2
            }
        ],
        "RequestId": "937055aa-1972-4bc1-9f6d-157a9fac537c"
    }
}
```

