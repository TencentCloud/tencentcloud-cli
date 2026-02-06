**Example 1: 查询实例的密码复杂度**

查询实例的密码复杂度

Input: 

```
tccli cdb DescribeInstancePasswordComplexity --cli-unfold-argument  \
    --InstanceId cdb-1urqrvpf
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CurrentValue": "8",
                "Default": "0",
                "Description": "The minimum number of characters that validate_password requires passwords to have.",
                "EnumValue": [],
                "IsNotSupportEdit": false,
                "Max": 64,
                "MaxFunc": "",
                "Min": 0,
                "MinFunc": "",
                "Name": "validate_password_length",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "1",
                "Default": "0",
                "Description": "The minimum number of lowercase and uppercase characters that validate_password requires passwords to have if the password policy is MEDIUM or stronger.",
                "EnumValue": [],
                "IsNotSupportEdit": false,
                "Max": 16,
                "MaxFunc": "",
                "Min": 0,
                "MinFunc": "",
                "Name": "validate_password_mixed_case_count",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "2",
                "Default": "0",
                "Description": "The minimum number of numeric (digit) characters that validate_password requires passwords to have if the password policy is MEDIUM or stronger.",
                "EnumValue": [],
                "IsNotSupportEdit": false,
                "Max": 16,
                "MaxFunc": "",
                "Min": 0,
                "MinFunc": "",
                "Name": "validate_password_number_count",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "MEDIUM",
                "Default": "LOW",
                "Description": "The password policy enforced by validate_password. The validate_password.policy value can be specified using numeric values 0, 1, 2.",
                "EnumValue": [
                    "LOW",
                    "MEDIUM",
                    "STRONG"
                ],
                "IsNotSupportEdit": false,
                "Max": 0,
                "MaxFunc": "",
                "Min": 0,
                "MinFunc": "",
                "Name": "validate_password_policy",
                "NeedReboot": 0,
                "ParamType": "enum"
            },
            {
                "CurrentValue": "3",
                "Default": "0",
                "Description": "The minimum number of nonalphanumeric characters that validate_password requires passwords to have if the password policy is MEDIUM or stronger.",
                "EnumValue": [],
                "IsNotSupportEdit": false,
                "Max": 16,
                "MaxFunc": "",
                "Min": 0,
                "MinFunc": "",
                "Name": "validate_password_special_char_count",
                "NeedReboot": 0,
                "ParamType": "integer"
            }
        ],
        "RequestId": "103be0cb-4ca7-400b-a6b1-4c3fc7b7227c",
        "TotalCount": 5
    }
}
```

