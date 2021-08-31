**Example 1: 获取高危命令规则列表**



Input: 

```
tccli cwp DescribeBashRules --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": 1,
                "Name": "xx",
                "Level": 1,
                "Hostip": "xx",
                "IsGlobal": 1,
                "Rule": "xx",
                "CreateTime": "xx",
                "Decription": "xx",
                "Uuids": [
                    "xx"
                ],
                "ModifyTime": "xx",
                "Operator": "xx",
                "White": 1,
                "DealOldEvents": 1,
                "Id": 1,
                "Uuid": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

