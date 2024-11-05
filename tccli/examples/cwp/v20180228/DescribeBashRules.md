**Example 1: 示例**

获取高危命令规则列表

Input: 

```
tccli cwp DescribeBashRules --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 1,
                "Uuid": "69E78F7F-FFC7-47D1-B406-13C9852******",
                "Name": "反弹shell",
                "Level": 3,
                "Rule": "ncat\\s+--ssl.*?\\/bin\\/bash",
                "Decription": "desc",
                "Operator": "root",
                "IsGlobal": 0,
                "Status": 0,
                "CreateTime": "2021-04-10 16:46:55",
                "ModifyTime": "2021-04-10 16:46:55",
                "Hostip": "10.0.1****",
                "White": 0,
                "Uuids": [
                    "d4cc302e-09e5-436f-b99b-5ab9c9070323"
                ],
                "DealOldEvents": 0,
                "Description": "desc"
            }
        ],
        "RequestId": "a0e9ed25-686e-452b-8dd1-ef25440c6543",
        "TotalCount": 1
    }
}
```

