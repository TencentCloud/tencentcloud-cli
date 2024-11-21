**Example 1: 查询本地专用集群云硬盘信息**

查询本地专用集群云硬盘信息

Input: 

```
tccli cdc DescribeDedicatedClusterCbsStatistics --cli-unfold-argument  \
    --DedicatedClusterId cluster-262n63e8
```

Output: 
```
{
    "Response": {
        "RequestId": "68dd812b-30ea-4d05-af65-be2bd13bd51e",
        "SetList": [
            {
                "Await": {
                    "Timestamps": [],
                    "Values": []
                },
                "CreateTime": "2022-12-09 15:20:09",
                "ReadIO": {
                    "Timestamps": [],
                    "Values": []
                },
                "ReadTraffic": {
                    "Timestamps": [],
                    "Values": []
                },
                "SetId": "set-mm4hzptu",
                "SetName": "HCBS_GZCDC_Z133_CDCCBS_Y0SH1125G_D0003",
                "SetSize": 33.4,
                "SetStatus": "RUNNING",
                "SetType": "ssd",
                "Util": {
                    "Timestamps": [],
                    "Values": []
                },
                "WriteIO": {
                    "Timestamps": [],
                    "Values": []
                },
                "WriteTraffic": {
                    "Timestamps": [],
                    "Values": []
                }
            }
        ],
        "TotalCount": 1
    }
}
```

