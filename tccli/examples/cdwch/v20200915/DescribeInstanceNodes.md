**Example 1: 获取实例节点信息列表**

获取实例节点信息列表

Input: 

```
tccli cdwch DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId cdwch-12345678
```

Output: 
```
{
    "Response": {
        "InstanceNodesList": [
            {
                "Cluster": "default_cluster",
                "Core": 2,
                "DiskSize": 200,
                "DiskType": "CLOUD_HSSD",
                "Ip": "10.0.0.x",
                "IsCHProxy": false,
                "Memory": 4,
                "NodeGroups": [],
                "RealResourceId": "ins-xxxxxxxx",
                "Rip": "9.0.x.x",
                "Spec": "S_2_4_H",
                "Status": "Running",
                "UUID": "939cd0af-b336-4e83-ad1f-1bc11ea097b",
                "Zone": "ap-chongqing-1",
                "ZoneDesc": "重庆一区"
            },
            {
                "Cluster": "default_cluster",
                "Core": 2,
                "DiskSize": 200,
                "DiskType": "CLOUD_HSSD",
                "Ip": "10.0.0.x",
                "IsCHProxy": false,
                "Memory": 4,
                "NodeGroups": [],
                "RealResourceId": "ins-xxxxxxxx",
                "Rip": "9.0.x.x",
                "Spec": "S_2_4_H",
                "Status": "Running",
                "UUID": "939cd0af-b336-4e83-ad1f-1bc11ea097b",
                "Zone": "ap-chongqing-1",
                "ZoneDesc": "重庆一区"
            }
        ],
        "RequestId": "xxxxxxxxxx",
        "TotalCount": 2
    }
}
```

