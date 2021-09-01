**Example 1: 获取暴力破解事件列表**

本接口{DescribeBruteAttacks}用于获取暴力破解事件列表。

Input: 

```
tccli yunjing DescribeBruteAttacks --cli-unfold-argument  \
    --Filters.0.Name Keywords \
    --Filters.0.Values Centos \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "BruteAttacks": [
            {
                "Id": "123",
                "Uuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1",
                "MachineIp": "127.0.0.1",
                "MachineName": "测试机",
                "Status": " BRUTEATTACK_SUCCESS",
                "Username": "root",
                "City": 1,
                "Country": 1,
                "Province": 1,
                "SrcIp": "127.0.0.1",
                "Count": 10,
                "CreateTime": "2018-01-01 12 :16:09"
            }
        ],
        "TotalCount": 100
    }
}
```

