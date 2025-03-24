**Example 1: 获取型号的填写模板**



Input: 

```
tccli chc DescribeModelTemplate --cli-unfold-argument  \
    --DeviceType server
```

Output: 
```
{
    "Response": {
        "RequestId": "1cb9293d-5bd1-4e2d-9dd3-d289b0d6c113",
        "TemplateDetail": [
            {
                "CompareType": "--",
                "InputHint": "",
                "InputInfo": "请注意节点数代表服务器子机数量，正常情况下标准服务器均为1",
                "InputType": "dropDown",
                "OptionKey": "DevNode",
                "OptionName": "节点数",
                "OptionValueSet": [
                    {
                        "OptionValue": "1",
                        "Selected": true
                    },
                    {
                        "OptionValue": "4",
                        "Selected": false
                    }
                ],
                "Standard": "--",
                "StandardInfo": "--",
                "ValueType": "number"
            },
            {
                "CompareType": "--",
                "InputHint": "填写设备高度（正整数，不带U）",
                "InputInfo": "",
                "InputType": "int",
                "OptionKey": "DevHeight",
                "OptionName": "高度(u)",
                "OptionValueSet": [],
                "Standard": "1u=44.45mm",
                "StandardInfo": "1u=44.45mm",
                "ValueType": "number"
            },
            {
                "CompareType": "<",
                "InputHint": "填写正整数",
                "InputInfo": "",
                "InputType": "int",
                "OptionKey": "PowerEnergy",
                "OptionName": "功耗(W)",
                "OptionValueSet": [],
                "Standard": "4400",
                "StandardInfo": "单柜<4400/6600",
                "ValueType": "number"
            }
        ]
    }
}
```

