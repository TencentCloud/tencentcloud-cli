**Example 1: InstanceEnumParam**

用户请求该接口获取其mongoDB实例可配置的参数列表；

Input: 

```
tccli mongodb DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId jyjcw8yv
```

Output: 
```
{
    "Response": {
        "InstanceEnumParam": [
            {
                "Status": 1,
                "CurrentValue": "xx",
                "DefaultValue": "xx",
                "NeedRestart": "xx",
                "EnumValue": [
                    "xx"
                ],
                "ParamName": "xx",
                "Tips": [
                    "xx"
                ],
                "ValueType": "xx"
            }
        ],
        "InstanceTextParam": [
            {
                "Status": "xx",
                "CurrentValue": "xx",
                "DefaultValue": "xx",
                "NeedRestart": "xx",
                "ParamName": "xx",
                "Tips": [
                    "xx"
                ],
                "TextValue": "xx",
                "ValueType": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx",
        "InstanceIntegerParam": [
            {
                "Status": 1,
                "CurrentValue": "xx",
                "Min": "xx",
                "Max": "xx",
                "DefaultValue": "xx",
                "NeedRestart": "xx",
                "ParamName": "xx",
                "Tips": [
                    "xx"
                ],
                "ValueType": "xx",
                "Unit": "xx"
            }
        ],
        "InstanceMultiParam": [
            {
                "Status": 1,
                "CurrentValue": "xx",
                "DefaultValue": "xx",
                "NeedRestart": "xx",
                "EnumValue": [
                    "xx"
                ],
                "ParamName": "xx",
                "Tips": [
                    "xx"
                ],
                "ValueType": "xx"
            }
        ]
    }
}
```

