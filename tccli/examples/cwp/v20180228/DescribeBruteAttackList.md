**Example 1: 获取密码破解列表**

获取密码破解列表

Input: 

```
tccli cwp DescribeBruteAttackList --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values abc \
    --Filters.0.Name abc \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "BruteAttackList": [
            {
                "Id": 202008000000971,
                "Uuid": "c2972dd6-165e-11ea-95eb-40f2e9f5667a",
                "MachineIp": "10.104.135.28",
                "MachineName": "poc测试-debian9",
                "UserName": "root",
                "SrcIp": "117.146.173.98",
                "Status": "FAILED",
                "EventType": 200,
                "Country": 1,
                "City": 334,
                "Province": 31,
                "CreateTime": "2020-02-21 16:35:49",
                "BanStatus": 82,
                "Count": 1098,
                "InstanceId": "ins-xxx"
            }
        ],
        "RequestId": "4234234",
        "TotalCount": 25328
    }
}
```

