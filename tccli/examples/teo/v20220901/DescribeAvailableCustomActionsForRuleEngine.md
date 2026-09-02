**Example 1: 查询规则引擎可用的定制配置列表**

查询站点下规则引擎可用的定制配置列表。

Input: 

```
tccli teo DescribeAvailableCustomActionsForRuleEngine --cli-unfold-argument  \
    --ZoneId zone-3**********x \
    --Filters.0.Name action-id \
    --Filters.0.Values ca-3**********n \
    --Limit 1 \
    --Offset 0 \
    --SortBy action-id \
    --SortOrder desc
```

Output: 
```
{
    "Response": {
        "CustomActionSet": [
            {
                "ActionId": "ca-3**********n",
                "Description": "Rate limiting for client IP access.",
                "Name": "ClientIPRateLimit",
                "Parameters": [
                    {
                        "Default": "100",
                        "Description": "The maximum QPS of the client IP",
                        "MaxValue": 10000,
                        "MinValue": 1,
                        "Name": "MaxQPS",
                        "Required": false,
                        "ValueType": "Integer"
                    }
                ],
                "SupportedConditions": [
                    "http.request.host"
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "bbd3abd8-aeb6-4ca5-a623-6502f8f19c1a"
    }
}
```

