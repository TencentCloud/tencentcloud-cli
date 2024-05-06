**Example 1: DescribeRulesSetting**



Input: 

```
tccli teo DescribeRulesSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Actions": [
            {
                "Action": "StatusCodeCache",
                "Properties": [
                    {
                        "Name": "CacheTime",
                        "Type": "CUSTOM_NUM",
                        "Min": 0,
                        "Max": 0,
                        "ChoicesValue": [],
                        "IsMultiple": false,
                        "IsAllowEmpty": false,
                        "ChoiceProperties": [],
                        "ExtraParameter": {
                            "Choices": [
                                "403",
                                "404",
                                "404",
                                "405",
                                "414",
                                "416",
                                "451",
                                "500",
                                "501",
                                "502",
                                "503",
                                "504"
                            ],
                            "Id": "StatusCode",
                            "Type": "CHOICE"
                        }
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

