**Example 1: 查询专用集群列表**

查询专用集群列表

Input: 

```
tccli cdc DescribeDedicatedClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DedicatedClusterSet": [
            {
                "DedicatedClusterId": "cluster-e88qh1ue",
                "Zone": "ap-guangzhou-2",
                "Description": "test",
                "Name": "wechen-first-dc",
                "LifecycleStatus": "PENDING",
                "CreateTime": "2020-12-10T06:15:43Z",
                "SiteId": "site-38d9ck"
            },
            {
                "DedicatedClusterId": "cluster-1hza0fbu",
                "Zone": "ap-guangzhou-2",
                "Description": "test",
                "Name": "wechen-first-dc",
                "LifecycleStatus": "PENDING",
                "CreateTime": "2020-12-10T06:15:50Z",
                "SiteId": "site-38d9ck"
            },
            {
                "DedicatedClusterId": "cluster-ptrfvhyw",
                "Zone": "ap-guangzhou-2",
                "Description": "test",
                "Name": "wechen-first-dc",
                "LifecycleStatus": "PENDING",
                "CreateTime": "2020-12-10T06:17:26Z",
                "SiteId": "site-38d9ck"
            }
        ],
        "TotalCount": 3,
        "RequestId": "92b47775-2f39-4ad0-b5dd-0a93a8f12636"
    }
}
```

