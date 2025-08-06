**Example 1: 请求网络设备的通用服务订单详情**



Input: 

```
tccli chc DescribeCommonServiceWorkOrderDetail --cli-unfold-argument  \
    --OrderId ord-25030712531166778
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "ContactName": "zhangsan",
            "ContactPhone": "13134567876",
            "IdcName": "天津数据备份中心东区4栋DC",
            "Instructions": "remark",
            "PreAuthorization": true,
            "ServiceLevel": 1
        },
        "DeviceSet": [
            {
                "DeviceType": "netDevice",
                "IdcName": "天津数据备份中心东区4栋DC",
                "IdcUnitName": "天津数据备份中心东区4栋DCM208",
                "RackName": "M208-C08",
                "Sn": "lhshenNet101"
            }
        ],
        "OrderStatus": "finish",
        "RequestId": "8df49659-bc07-4364-ab1b-2c5981d3ab61",
        "StepSet": [
            {
                "FinishTime": "2025-03-07 12:53:11",
                "OwnerName": "zhangsan",
                "StepName": "发起申请",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "2025-03-07 13:02:37",
                "OwnerName": "",
                "StepName": "现场实施",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "",
                "OwnerName": "",
                "StepName": "客户验证确认",
                "StepStatus": "processing"
            }
        ]
    }
}
```

