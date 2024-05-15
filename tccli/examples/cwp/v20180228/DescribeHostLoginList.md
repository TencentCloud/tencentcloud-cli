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
                "ModifyTime": "2020-02-20 14:51:35",
                "IsRiskUser": 0,
                "Port": 22,
                "Location": "中国:广东省:深圳市",
                "Desc": "",
                "IsRiskSrcIp": 1,
                "IsRiskArea": 1,
                "Quuid": "xxxx-xxxx-xxxxxx-xxxxxx-xxxx",
                "RiskLevel": 0,
                "IsRiskTime": 1,
                "MachineExtraInfo": {
                    "WanIP": "111.111.111.111",
                    "InstanceID": "ins-12341234",
                    "NetworkName": "",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 1,
                    "HostName": "abc"
                }
            }
        ],
        "RequestId": "4234234",
        "TotalCount": 446
    }
}
```

