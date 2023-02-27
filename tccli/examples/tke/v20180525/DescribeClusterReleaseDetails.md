**Example 1: 查询集群已安装应用详情**

查询集群已安装应用详情

Input: 

```
tccli tke DescribeClusterReleaseDetails --cli-unfold-argument  \
    --Namespace default \
    --ClusterId cls-65r1c5nu \
    --Name app-name
```

Output: 
```
{
    "Response": {
        "Release": {
            "Name": "app-name",
            "Namespace": "default",
            "Version": "1",
            "Status": "deployed",
            "Description": "Install complete",
            "Notes": "",
            "Config": "key1=v1,key2=v2",
            "Manifest": "",
            "ChartVersion": "10.5.3",
            "ChartName": "redis",
            "ChartDescription": "Open source, advanced key-value store. It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets.",
            "AppVersion": "5.0.7",
            "FirstDeployedTime": "2020-04-09 15:28:28.707549 +0800 CST",
            "LastDeployedTime": "2020-04-09 15:28:28.707549 +0800 CST"
        },
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

