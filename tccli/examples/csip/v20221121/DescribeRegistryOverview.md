**Example 1: 查询仓库总览**



Input: 

```
tccli csip DescribeRegistryOverview --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "RegistryConnectFailedCount": 0,
        "RegistryCount": 14,
        "RegistryTypeList": [
            {
                "Count": 12,
                "RegistryType": "ccr"
            }
        ],
        "RequestId": "fa62e68d-9180-41df-a549-0b9d708f54b5"
    }
}
```

