**Example 1: 查看服务器设备型号评估工单详情**



Input: 

```
tccli chc DescribeModelEvaluationWorkOrderDetail --cli-unfold-argument  \
    --OrderId ord-25030519265285037
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "CampusName": "天津-武清",
            "CustomerName": "某某公司",
            "DeviceType": "server",
            "Remark": "zhangsan"
        },
        "NetDeviceModelSet": [],
        "OrderStatus": "finish",
        "RequestId": "8ca708b5-695c-4c2d-be1a-39dd5c559710",
        "ServerModelSet": [
            {
                "CheckResult": 1,
                "ModelVersion": "LHSHEN T2121 S5-V1",
                "OptionSet": [
                    {
                        "CompareType": "--",
                        "InputHint": "",
                        "InputInfo": "请注意节点数代表服务器子机数量，正常情况下标准服务器均为1",
                        "InputType": "dropDown",
                        "OptionKey": "devNode",
                        "OptionName": "节点数",
                        "OptionValue": "1",
                        "Standard": "--",
                        "StandardInfo": "--",
                        "ValueType": "number"
                    },
                    {
                        "CompareType": "--",
                        "InputHint": "填写设备高度（正整数，不带U）",
                        "InputInfo": "",
                        "InputType": "int",
                        "OptionKey": "devHeight",
                        "OptionName": "高度(u)",
                        "OptionValue": "22",
                        "Standard": "1u=44.45mm",
                        "StandardInfo": "1u=44.45mm",
                        "ValueType": "number"
                    },
                    {
                        "CompareType": "<",
                        "InputHint": "填写正整数",
                        "InputInfo": "",
                        "InputType": "int",
                        "OptionKey": "powerEnergy",
                        "OptionName": "功耗(W)",
                        "OptionValue": "330",
                        "Standard": "4400",
                        "StandardInfo": "单柜<4400/6600",
                        "ValueType": "number"
                    }
                ]
            }
        ],
        "StepSet": [
            {
                "FinishTime": "2025-03-05 19:26:52",
                "OwnerName": "zhangsan",
                "StepName": "发起申请",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "2025-03-05 19:36:24",
                "OwnerName": "lisi",
                "StepName": "现场实施",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "2025-03-05 19:36:24",
                "OwnerName": "",
                "StepName": "结单",
                "StepStatus": "finish"
            }
        ]
    }
}
```

