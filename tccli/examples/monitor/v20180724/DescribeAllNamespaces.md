**Example 1: 获得所有名字空间**



Input: 

```
tccli monitor DescribeAllNamespaces --cli-unfold-argument  \
    --AppId 12312312 \
    --Uin 123123123123 \
    --SubAccountUin 12312312313 \
    --Action DescribeAllNamespaces \
    --Version 2018-07-24 \
    --Region ap-guangzhou \
    --Module monitor \
    --Language zh-CN \
    --MonitorTypes MT_QCE MT_CUSTOM \
    --SceneType ST_ALARM
```

Output: 
```
{
    "Response": {
        "QceNamespace": [
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
        "CustomNamespace": [
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
        "RequestId": "d96ec542-6547-4af2-91ac-fee85c1b8b85"
    }
}
```

