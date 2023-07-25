**Example 1: 查询云产品交互类型**

查询云产品交互类型

Input: 

```
tccli smp DescribeProductInputType --cli-unfold-argument  \
    --ProductCode p_ccn \
    --SubProductCode 
```

Output: 
```
{
    "Response": {
        "RequestId": "02667663-b109-4ec0-a325-62deeb4e4ca1",
        "Data": {
            "Id": "7",
            "ProductCode": "p_ccn",
            "TypeName": "t_ccn",
            "InputJson": [
                {
                    "InputType": "Select",
                    "FieldKey": "ServiceLevel",
                    "DataType": "Enum",
                    "Name": "服务等级",
                    "Enum": [
                        {
                            "EnumKey": "Default",
                            "EnumValue": "金"
                        },
                        {
                            "EnumKey": "Platinum",
                            "EnumValue": "白金"
                        },
                        {
                            "EnumKey": "Silver",
                            "EnumValue": "银"
                        }
                    ],
                    "Required": true,
                    "Default": "Default",
                    "Unit": ""
                },
                {
                    "InputType": "Input",
                    "FieldKey": "ResourceId",
                    "DataType": "String",
                    "Name": "资源ID",
                    "Enum": [],
                    "Required": true,
                    "Default": "",
                    "Unit": ""
                },
                {
                    "InputType": "MonthDate",
                    "FieldKey": "DownMonth",
                    "DataType": "String",
                    "Name": "故障发生月份",
                    "Enum": [],
                    "Required": true,
                    "Default": "",
                    "Unit": ""
                },
                {
                    "InputType": "Input",
                    "FieldKey": "DownTime",
                    "DataType": "Integer",
                    "Name": "不可用服务时间",
                    "Enum": [],
                    "Required": true,
                    "Default": "",
                    "Unit": "分钟"
                }
            ]
        }
    }
}
```

