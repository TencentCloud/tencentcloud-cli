**Example 1: 查询预留列表**

查询预留列表

Input: 

```
tccli goosefs DescribeCvmResource --cli-unfold-argument  \
    --OwnerUin 3472213910
```

Output: 
```
{
    "Response": {
        "RequestId": "fce51a31-20af-4c47-a388-daf868a4a0f0",
        "ResourceInstanceList": [
            {
                "BuildTime": "2024-09-12T20:05:49+08:00",
                "InstanceId": "ins-8dfjsthe",
                "InstanceType": "S5.2XLARGE16",
                "NodeType": "owner_cluster_nsd_node",
                "OwnerUin": 3472213910,
                "Region": "ap-nanjing",
                "Zone": "ap-nanjing-1"
            },
            {
                "BuildTime": "2024-09-12T20:05:59+08:00",
                "InstanceId": "ins-cuase21u",
                "InstanceType": "S5.2XLARGE16",
                "NodeType": "owner_cluster_nsd_node",
                "OwnerUin": 3472213910,
                "Region": "ap-nanjing",
                "Zone": "ap-nanjing-1"
            },
            {
                "BuildTime": "2024-09-12T20:05:49+08:00",
                "InstanceId": "ins-gzy36j64",
                "InstanceType": "S5.2XLARGE16",
                "NodeType": "owner_cluster_nsd_node",
                "OwnerUin": 3472213910,
                "Region": "ap-nanjing",
                "Zone": "ap-nanjing-1"
            }
        ],
        "TotalCount": 3
    }
}
```

