**Example 1: 空示例**

空示例

Input: 

```
tccli csip DescribeClusterPodAssets --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 0,
                "Uin": "abc",
                "Nick": "abc",
                "Region": "abc",
                "AssetId": "abc",
                "AssetName": "abc",
                "InstanceCreateTime": "abc",
                "Namespace": "abc",
                "PublicIp": "abc",
                "PrivateIp": "abc",
                "Status": "abc",
                "ClusterId": "abc",
                "ClusterName": "abc",
                "MachineId": "abc",
                "MachineName": "abc",
                "PodIp": "abc",
                "ServiceCount": 0,
                "ContainerCount": 0
            }
        ],
        "TotalCount": 0,
        "PodStatusList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RegionList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "AppIdList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "NamespaceList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

