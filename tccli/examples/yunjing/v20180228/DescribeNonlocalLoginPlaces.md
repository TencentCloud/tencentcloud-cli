**Example 1: 获取异地登录事件**

本接口（DescribeNonlocalLoginPlaces）用于获取异地登录事件。

Input: 

```
tccli yunjing DescribeNonlocalLoginPlaces --cli-unfold-argument  \
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
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "NonLocalLoginPlaces": [
            {
                "Id": 123,
                "Uuid": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
                "MachineIp": "127.0.0.1",
                "MachineName": "machine-name",
                "Status": "NON_LOCAL_LOGIN",
                "Username": "root",
                "City": 1,
                "Country": 1,
                "Province": 1,
                "SrcIp": "127.0.0.1",
                "LoginTime": "2018-07-18 12:16:09"
            }
        ],
        "TotalCount": 100
    }
}
```

