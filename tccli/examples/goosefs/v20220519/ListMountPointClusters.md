**Example 1: 列举集群信息**



Input: 

```
tccli goosefs ListMountPointClusters --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClientCount": {
                    "Running": 0,
                    "Stopped": 0,
                    "Total": 0
                },
                "ClusterId": "clst-gcUwDSBZ",
                "CreateTime": 1782963773,
                "Description": "test desc",
                "Name": "test-probe2",
                "Networks": {
                    "VpcIds": []
                },
                "NodeCount": {
                    "Offline": 0,
                    "Online": 0,
                    "Total": 0
                },
                "Region": "ap-guangzhou",
                "UpdateTime": 1782963773
            }
        ],
        "TotalCount": 99,
        "RequestId": "b57b384c-6529-41b9-85f6-3b38a8f84b42"
    }
}
```

