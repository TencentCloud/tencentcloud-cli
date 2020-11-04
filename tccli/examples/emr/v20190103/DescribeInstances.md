**Example 1: 查询实例详情**



Input: 

```
tccli emr DescribeInstances --cli-unfold-argument  \
    --Offset 0\
    --Limit 10\
    --ProjectId 0\
    --OrderField clusterid\
    --Asc 0\
    --DisplayStrategy clusterList\
    --InstanceIds emr-p9f700x8
```

Output: 
```
{
    "Response": {
        "ClusterList": [
            {
                "AddTime": "2019-09-16 16:48:01",
                "AlarmInfo": "",
                "AppId": 251008830,
                "ChargeType": 1,
                "ClusterId": "emr-p9f700x8",
                "ClusterName": "beckwu_包年勿删",
                "Config": {
                    "ChargeType": 1,
                    "ComNodeSize": 0,
                    "ComResource": {
                        "Cpu": 0,
                        "DiskSize": 0,
                        "DiskType": "",
                        "MemSize": 0,
                        "RootSize": 0,
                        "Spec": "",
                        "SpecName": "",
                        "StorageType": 0
                    },
                    "CoreNodeSize": 2,
                    "CoreResource": {
                        "Cpu": 2,
                        "DiskSize": 100,
                        "DiskType": "CLOUD_BASIC",
                        "MemSize": 8192,
                        "RootSize": 0,
                        "Spec": "CVM.S2",
                        "SpecName": "EMR标准型S2",
                        "StorageType": 2
                    },
                    "MasterNodeSize": 1,
                    "MasterResource": {
                        "Cpu": 2,
                        "DiskSize": 100,
                        "DiskType": "CLOUD_BASIC",
                        "MemSize": 8192,
                        "RootSize": 0,
                        "Spec": "CVM.S2",
                        "SpecName": "EMR标准型S2",
                        "StorageType": 2
                    },
                    "OnCos": false,
                    "SoftInfo": [
                        "zookeeper-3.4.9",
                        "hadoop-3.1.2",
                        "knox-1.2.0",
                        "sys-1.0"
                    ],
                    "TaskNodeSize": 1,
                    "TaskResource": {
                        "Cpu": 2,
                        "DiskSize": 100,
                        "DiskType": "CLOUD_BASIC",
                        "MemSize": 8192,
                        "RootSize": 0,
                        "Spec": "CVM.S2",
                        "SpecName": "EMR标准型S2",
                        "StorageType": 2
                    }
                },
                "EmrVersion": "EMR-V3.0.0",
                "Ftitle": "集群运行中",
                "Id": 19541,
                "IsTradeCluster": 0,
                "MasterIp": "--",
                "ProjectId": 0,
                "RegionId": 1,
                "ResourceOrderId": 0,
                "RunTime": "0天2小时48分钟55秒",
                "Status": 2,
                "SubnetId": 1230738,
                "TradeVersion": 1,
                "Uin": "1875765535",
                "VpcId": 78518,
                "ZoneId": 100002
            }
        ],
        "RequestId": "4f337873-6fea-4338-9715-24f539b60949",
        "TotalCnt": 1
    }
}
```

