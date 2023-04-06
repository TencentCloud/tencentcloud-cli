**Example 1: 查询集群已安装应用列表**

展示应用列表

Input: 

```
tccli tke DescribeClusterReleases --cli-unfold-argument  \
    --ClusterId cls-65r1c5nu
```

Output: 
```
{
    "Response": {
        "Limit": 0,
        "Offset": 0,
        "ReleaseSet": [
            {
                "Name": "app-name",
                "Namespace": "default",
                "Revision": "1",
                "Status": "deployed",
                "ChartName": "redis",
                "ChartVersion": "10.5.3",
                "AppVersion": "5.0.7",
                "UpdatedTime": "2020-04-09 15:28:28.707549 +0800 CST"
            }
        ],
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2",
        "Total": 1
    }
}
```

