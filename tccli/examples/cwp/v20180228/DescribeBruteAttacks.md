**Example 1: 获取暴力破解事件列表**

本接口{DescribeBruteAttacks}用于获取暴力破解事件列表。

Input: 

```
tccli cwp DescribeBruteAttacks --cli-unfold-argument  \
    --Filters.0.Name Keywords \
    --Filters.0.Values Centos \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BruteAttacks": [
            {
                "Status": "xx",
                "UserName": "xx",
                "IsProVersion": true,
                "MachineIp": "xx",
                "Uuid": "xx",
                "City": 1,
                "BanStatus": "xx",
                "Country": 1,
                "Id": 1,
                "Count": 1,
                "Quuid": "xx",
                "MachineName": "xx",
                "SrcIp": "xx",
                "CreateTime": "2020-09-22 00:00:00",
                "Province": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

