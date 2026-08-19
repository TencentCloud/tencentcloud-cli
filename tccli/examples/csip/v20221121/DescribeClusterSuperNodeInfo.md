**Example 1: 超级节点详情信息**



Input: 

```
tccli csip DescribeClusterSuperNodeInfo --cli-unfold-argument  \
    --NodeUniqueID 208a70484c9f8ac0ce43d896d406081d
```

Output: 
```
{
    "Response": {
        "AppID": 260083796,
        "AssetSyncTime": "2026-08-09T06:05:40Z",
        "ClusterId": "cls-pde9e0s0",
        "ClusterName": "yancyw-标准集群",
        "ClusterVersion": "1.30.0",
        "CoresCount": 4000,
        "InstanceId": "kn-1ogxmons",
        "KubeletVersion": "v2.16.78",
        "NodeName": "未命名",
        "NodeSource": "TKE_MANAGED_CLUSTER",
        "Region": "ap-guangzhou",
        "RegionName": "华南地区（广州）",
        "RegionNameEn": "South China (Guangzhou)",
        "Status": "Running",
        "SubNetCIDR": "172.16.0.0/20",
        "SubNetId": "subnet-9hwe9oeo",
        "SubNetName": "",
        "VpcId": "vpc-nk47l8at",
        "Zone": "广州二区",
        "RequestId": "b7effa7d-34b0-4e7a-a3f8-b4b1943fa383"
    }
}
```

