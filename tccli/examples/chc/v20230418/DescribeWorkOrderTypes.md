**Example 1: 请求示例**



Input: 

```
tccli chc DescribeWorkOrderTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CollectedWorkOderTypeSet": [
            {
                "CollectFlag": true,
                "SlaMessage": "2个工作日",
                "WorkOrderDescription": "客户设备托管到腾讯IDC机房，为了确保设备符合机房的上架标准， 在入场前，需要提前进行托管设备入场的评估。",
                "WorkOrderFamily": "设备服务",
                "WorkOrderName": "托管设备型号评估",
                "WorkOrderType": "modelEvaluation"
            },
            {
                "CollectFlag": true,
                "SlaMessage": "2 个工作日",
                "WorkOrderDescription": "提供现场外包资产管理员，进行现场物资的收货和验收操作。\n",
                "WorkOrderFamily": "设备服务",
                "WorkOrderName": "设备收货",
                "WorkOrderType": "receiving"
            },
            {
                "CollectFlag": true,
                "SlaMessage": "2 个工作日",
                "WorkOrderDescription": "提供现场外包工程师，将指定设备上到机位上。 ",
                "WorkOrderFamily": "设备服务",
                "WorkOrderName": "设备上架",
                "WorkOrderType": "rackOn"
            },
            {
                "CollectFlag": true,
                "SlaMessage": "最快 2 个工作日",
                "WorkOrderDescription": "提供设备的开电操作。机架的开电由IDC平台部数经判断，自行发起。\n",
                "WorkOrderFamily": "设备服务",
                "WorkOrderName": "设备开电",
                "WorkOrderType": "powerOn"
            },
            {
                "CollectFlag": true,
                "SlaMessage": "最快 1 个工作日",
                "WorkOrderDescription": "根据客户要求， 在同IDC内对指定设备进行搬迁操作。",
                "WorkOrderFamily": "设备服务",
                "WorkOrderName": "机房内搬迁",
                "WorkOrderType": "moving"
            }
        ],
        "RequestId": "3dad52cf-67c5-4eed-b191-e4f542ce4d80",
        "WorkOrderFamilySet": [
            {
                "WorkOrderFamily": "设备服务",
                "WorkOrderTypeSet": [
                    {
                        "CollectFlag": true,
                        "SlaMessage": "2个工作日",
                        "WorkOrderDescription": "客户设备托管到腾讯IDC机房，为了确保设备符合机房的上架标准， 在入场前，需要提前进行托管设备入场的评估。",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "托管设备型号评估",
                        "WorkOrderType": "modelEvaluation"
                    },
                    {
                        "CollectFlag": true,
                        "SlaMessage": "2 个工作日",
                        "WorkOrderDescription": "提供现场外包资产管理员，进行现场物资的收货和验收操作。\n",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "设备收货",
                        "WorkOrderType": "receiving"
                    },
                    {
                        "CollectFlag": true,
                        "SlaMessage": "2 个工作日",
                        "WorkOrderDescription": "提供现场外包工程师，将指定设备上到机位上。 ",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "设备上架",
                        "WorkOrderType": "rackOn"
                    },
                    {
                        "CollectFlag": true,
                        "SlaMessage": "最快 2 个工作日",
                        "WorkOrderDescription": "提供设备的开电操作。机架的开电由IDC平台部数经判断，自行发起。\n",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "设备开电",
                        "WorkOrderType": "powerOn"
                    },
                    {
                        "CollectFlag": true,
                        "SlaMessage": "最快 1 个工作日",
                        "WorkOrderDescription": "根据客户要求， 在同IDC内对指定设备进行搬迁操作。",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "机房内搬迁",
                        "WorkOrderType": "moving"
                    },
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快 2 个工作日",
                        "WorkOrderDescription": "提供设备的关电操作。\n",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "设备关电",
                        "WorkOrderType": "powerOff"
                    },
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快当天完成",
                        "WorkOrderDescription": "提供现场外包工程师，将指定设备从机位上下架。",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "设备下架",
                        "WorkOrderType": "rackOff"
                    },
                    {
                        "CollectFlag": false,
                        "SlaMessage": "1 个工作日",
                        "WorkOrderDescription": "客户将设备等资产迁出腾讯机房， 腾讯提供指定设备的交接服务， 不包含物流服务，不包含包装、搬车和装运服务。",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "退出交接",
                        "WorkOrderType": "quit"
                    },
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快 2 个工作日",
                        "WorkOrderDescription": "提供机架的开电操作。",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "机架开电",
                        "WorkOrderType": "rackPowerOn"
                    },
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快 2 个工作日",
                        "WorkOrderDescription": "提供机架的关电操作。",
                        "WorkOrderFamily": "设备服务",
                        "WorkOrderName": "机架关电",
                        "WorkOrderType": "rackPowerOff"
                    }
                ]
            },
            {
                "WorkOrderFamily": "人员服务",
                "WorkOrderTypeSet": [
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快 1 个工作日",
                        "WorkOrderDescription": "非机房常驻运维及授权人员，因运维需要进入机房，需提交人员到访申请。",
                        "WorkOrderFamily": "人员服务",
                        "WorkOrderName": "人员到访",
                        "WorkOrderType": "personnelVisit"
                    }
                ]
            },
            {
                "WorkOrderFamily": "通用服务",
                "WorkOrderTypeSet": [
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快 30min 响应",
                        "WorkOrderDescription": "提供网络设备的设备重启、状态查看等通用服务受理",
                        "WorkOrderFamily": "通用服务",
                        "WorkOrderName": "网络设备通用服务",
                        "WorkOrderType": "netDeviceCommon"
                    },
                    {
                        "CollectFlag": false,
                        "SlaMessage": "最快 30min 响应",
                        "WorkOrderDescription": "提供服务器的设备重启、插拔硬盘、重装系统、状态查看等通用服务受理",
                        "WorkOrderFamily": "通用服务",
                        "WorkOrderName": "服务器通用服务",
                        "WorkOrderType": "serverCommon"
                    }
                ]
            }
        ]
    }
}
```

