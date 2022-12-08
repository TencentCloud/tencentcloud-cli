**Example 1: 查询集群安装中应用列表**



Input: 

```
tccli tke DescribeClusterPendingReleases --cli-unfold-argument  \
    --Limit 1 \
    --ClusterId cls-65r1c5nu
```

Output: 
```
{
    "Response": {
        "Limit": 1,
        "Offset": 0,
        "ReleaseSet": [
            {
                "Condition": "install release error: host must be a URL or a host:port pair: \"https://\"",
                "CreatedTime": "2020-04-15T09:07:22Z",
                "ID": "8aa09a63-8b9a-461f-8c5b-bd7872abdc37",
                "Name": "app-01",
                "Namespace": "lwj",
                "Status": "failed",
                "UpdatedTime": "2020-04-15T09:07:22Z"
            }
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01",
        "Total": 1
    }
}
```

