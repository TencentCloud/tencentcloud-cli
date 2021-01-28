**Example 1: 获取异地登录事件**

本接口（DescribeNonlocalLoginPlaces）用于获取异地登录事件。

Input: 

```
tccli cwp DescribeNonlocalLoginPlaces --cli-unfold-argument  \
    --Uuid 354f4ac3-8546-4516-8c8a-69e3ab73aa8a \
    --Filters.0.Name Keyword \
    --Filters.0.Values Centos \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "NonLocalLoginPlaces": [
            {
                "Status": "xx",
                "UserName": "xx",
                "Uuid": "xx",
                "City": 1,
                "Country": 1,
                "LoginTime": "2020-09-22 00:00:00",
                "Id": 1,
                "MachineName": "xx",
                "SrcIp": "xx",
                "MachineIp": "xx",
                "Province": 1
            }
        ]
    }
}
```

