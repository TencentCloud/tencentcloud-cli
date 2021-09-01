**Example 1: 获取帐号变更历史列表**

获取帐号变更历史列表

Input: 

```
tccli cwp DescribeHistoryAccounts --cli-unfold-argument  \
    --Uuid 6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1 \
    --Filters.0.Name MachineIp \
    --Filters.0.Values 10.0.1.1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "HistoryAccounts": [
            {
                "Id": 1,
                "Uuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1",
                "MachineName": "machine-name",
                "MachineIp": "10.104.86.62",
                "Username": "nginx",
                "ModifyType": "CREATE",
                "ModifyTime": "2018-01-01 12:12:12"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

