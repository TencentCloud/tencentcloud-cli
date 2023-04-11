**Example 1: 登录审计列表**

登录审计列表

Input: 

```
tccli cwp DescribeHostLoginList --cli-unfold-argument  \
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
        "HostLoginList": [
            {
                "Id": 202008000000022,
                "Uuid": "5cc8e4d2-311f-11ea-922b-98be9421969a",
                "MachineIp": "10.104.194.49",
                "MachineName": "v_lwjlin_centos_林",
                "UserName": "root",
                "SrcIp": "120.229.227.225",
                "Status": 2,
                "Country": 1,
                "City": 216,
                "Province": 19,
                "LoginTime": "2020-02-20 14:51:35",
                "ModifyTime": "2020-02-20 14:51:35"
            }
        ],
        "RequestId": "4234234",
        "TotalCount": 446
    }
}
```

