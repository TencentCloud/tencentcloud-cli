**Example 1: 集群pod列表**

集群pod列表

Input: 

```
tccli csip DescribeClusterPodAssets --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Filter.Limit 1 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1302396211",
                "Value": "1302396211"
            }
        ],
        "Data": [
            {
                "AppId": 1302396211,
                "AssetId": "002a244ad33***6b7ec01b91ae63a9",
                "AssetName": "kubernetes-proxy-6dd44f7b74-mqf4n",
                "ClusterId": "cls-0hdxu91s",
                "ClusterName": "yancyw",
                "ContainerCount": 1,
                "InstanceCreateTime": "2024-08-22 21:45:10",
                "IsCore": 2,
                "IsNewAsset": 0,
                "MachineId": "ins-0hdxu91s",
                "MachineName": "my-vm",
                "Namespace": "default",
                "Nick": "声声乌龙",
                "PodIp": "10.**.0.**",
                "PrivateIp": "10.**.0.**",
                "PublicIp": "118.**.**.**",
                "Region": "ap-guangzhou",
                "ServiceCount": 1,
                "Status": "Running",
                "Uin": "100014111178"
            }
        ],
        "NamespaceList": [
            {
                "Text": "default",
                "Value": "default"
            },
            {
                "Text": "kube-system",
                "Value": "kube-system"
            },
            {
                "Text": "tcss",
                "Value": "tcss"
            }
        ],
        "PodStatusList": [
            {
                "Text": "running",
                "Value": "running"
            },
            {
                "Text": "succeeded",
                "Value": "succeeded"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "077d335a-f2c7-4f20-884a-9700086f3608",
        "TotalCount": 27
    }
}
```

