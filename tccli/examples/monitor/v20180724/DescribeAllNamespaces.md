**Example 1: 获得所有名字空间**



Input: 

```
tccli monitor DescribeAllNamespaces --cli-unfold-argument  \
    --Module monitor \
    --MonitorTypes MT_QCE \
    --SceneType ST_ALARM
```

Output: 
```
{
    "Response": {
        "QceNamespaces": {
            "Id": "",
            "Name": "",
            "ProductName": "",
            "Value": "",
            "Config": "",
            "AvailableRegions": [],
            "DashboardId": "",
            "SortId": 0
        },
        "QceNamespacesNew": [
            {
                "Id": "xxxxxxx",
                "Name": "专线接入-专用通道",
                "ProductName": "专线接入-专用通道",
                "Value": "qce/dcx",
                "Config": "……",
                "AvailableRegions": [
                    "gz",
                    "sh"
                ],
                "DashboardId": "dcchannel",
                "SortId": 500
            }
        ],
        "CustomNamespaces": {
            "Id": "",
            "Name": "",
            "ProductName": "",
            "Value": "",
            "Config": "",
            "AvailableRegions": [],
            "DashboardId": "",
            "SortId": 0
        },
        "CustomNamespacesNew": [
            {
                "Id": "=wenlong_sidecar",
                "Name": "=wenlong_sidecar",
                "ProductName": "=wenlong_sidecar",
                "Value": "=wenlong_sidecar",
                "Config": "",
                "AvailableRegions": [],
                "DashboardId": "=wenlong_sidecar",
                "SortId": 0
            }
        ],
        "CommonNamespaces": [
            {
                "Id": "performance_metric",
                "MonitorType": "MT_TAW",
                "Name": "性能指标",
                "Dimensions": []
            }
        ],
        "RequestId": "d96ec542-6547-4af2-91ac-fee85c1b8b85"
    }
}
```

