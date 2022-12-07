**Example 1: 查询集群已安装应用版本历史**



Input: 

```
tccli tke DescribeClusterReleaseHistory --cli-unfold-argument  \
    --Namespace default \
    --ClusterId cls-65r1c5nu \
    --Name app-name
```

Output: 
```
{
    "Response": {
        "ReleaseHistorySet": [
            {
                "Name": "app-name",
                "Namespace": "default",
                "Revision": "1",
                "Status": "deployed",
                "Chart": "redis-10.5.3",
                "AppVersion": "5.0.7",
                "UpdatedTime": "2020-04-09 15:28:28.707549 +0800 CST",
                "Description": ""
            }
        ],
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2",
        "Total": 1
    }
}
```

