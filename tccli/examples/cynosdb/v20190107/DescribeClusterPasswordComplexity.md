**Example 1: 查看集群密码复杂度详情**



Input: 

```
tccli cynosdb DescribeClusterPasswordComplexity --cli-unfold-argument  \
    --ClusterId cynosdbmysql-bzxxrmtq
```

Output: 
```
{
    "Response": {
        "RequestId": "7613eed6-5eb5-4d17-ae69-dd93c44d7ad4",
        "ValidatePasswordDictionary": {
            "CurrentValue": "",
            "Default": "",
            "Description": "The dictionary words that validate_password uses for checking passwords.",
            "EnumValue": [],
            "IsGlobal": 0,
            "MatchType": "",
            "MatchValue": "",
            "Max": "0",
            "Min": "0",
            "ModifiableInfo": {},
            "NeedReboot": 0,
            "ParamName": "validate_password_txsql_dictionary",
            "ParamType": "string"
        },
        "ValidatePasswordLength": {
            "CurrentValue": "0",
            "Default": "8",
            "Description": "The minimum number of characters that validate_password requires passwords to have.",
            "EnumValue": [],
            "IsGlobal": 0,
            "MatchType": "",
            "MatchValue": "",
            "Max": "256",
            "Min": "8",
            "ModifiableInfo": {},
            "NeedReboot": 0,
            "ParamName": "validate_password_length",
            "ParamType": "integer"
        },
        "ValidatePasswordMixedCaseCount": {
            "CurrentValue": "0",
            "Default": "1",
            "Description": "The minimum number of lowercase and uppercase characters that validate_password requires passwords to have if the password policy is MEDIUM or stronger.",
            "EnumValue": [],
            "IsGlobal": 0,
            "MatchType": "",
            "MatchValue": "",
            "Max": "50",
            "Min": "1",
            "ModifiableInfo": {},
            "NeedReboot": 0,
            "ParamName": "validate_password_mixed_case_count",
            "ParamType": "integer"
        },
        "ValidatePasswordNumberCount": {
            "CurrentValue": "0",
            "Default": "1",
            "Description": "The minimum number of numeric (digit) characters that validate_password requires passwords to have if the password policy is MEDIUM or stronger. ",
            "EnumValue": [],
            "IsGlobal": 0,
            "MatchType": "",
            "MatchValue": "",
            "Max": "50",
            "Min": "1",
            "ModifiableInfo": {},
            "NeedReboot": 0,
            "ParamName": "validate_password_number_count",
            "ParamType": "integer"
        },
        "ValidatePasswordPolicy": {
            "CurrentValue": "LOW",
            "Default": "MEDIUM",
            "Description": "The password policy enforced by validate_password.",
            "EnumValue": [
                "MEDIUM",
                "STRONG"
            ],
            "IsGlobal": 0,
            "MatchType": "",
            "MatchValue": "",
            "Max": "2",
            "Min": "0",
            "ModifiableInfo": {},
            "NeedReboot": 0,
            "ParamName": "validate_password_policy",
            "ParamType": "enum"
        },
        "ValidatePasswordSpecialCharCount": {
            "CurrentValue": "0",
            "Default": "1",
            "Description": "The minimum number of nonalphanumeric characters that validate_password requires passwords to have if the password policy is MEDIUM or stronger. ",
            "EnumValue": [],
            "IsGlobal": 0,
            "MatchType": "",
            "MatchValue": "",
            "Max": "50",
            "Min": "1",
            "ModifiableInfo": {},
            "NeedReboot": 0,
            "ParamName": "validate_password_special_char_count",
            "ParamType": "integer"
        }
    }
}
```

