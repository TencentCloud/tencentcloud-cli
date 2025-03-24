**Example 1: 查看服务器设备型号详情**



Input: 

```
tccli chc DescribeModel --cli-unfold-argument  \
    --DevModel IBM X3650 M5007 \
    --CampusId 163 \
    --DeviceType server
```

Output: 
```
{
    "Response": {
        "ModelSet": [
            {
                "CheckResult": 0,
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
                        "OptionValue": "699",
                        "Standard": "4400",
                        "StandardInfo": "单柜<4400/6600",
                        "ValueType": "number"
                    }
                ],
                "Version": "V1"
            }
        ],
        "RequestId": "c1957d1a-3d98-4463-83ee-d12896ab5bde"
    }
}
```

