**Example 1: DescribeIotDevice**



Input: 

```
tccli iecp DescribeIotDevice --cli-unfold-argument  \
    --DeviceId 100049
```

Output: 
```
{
    "Response": {
        "UserName": "SA4RZ3NLIMlink01;21010406;MPWMB;1965121722",
        "Psk": "TTM5RjJCRTdSQUxOQkk3SA==",
        "Version": "",
        "Name": "link01",
        "UnitName": "ccccx",
        "LogLevel": 1,
        "Region": "ap-guangzhou",
        "PrivateKey": "",
        "ClientID": "SA4RZ3NLIMlink01",
        "Status": 1,
        "Disabled": true,
        "Cert": "",
        "PskHex": "4d3339463242453752414c4e42493748",
        "LogSetting": 1,
        "RequestId": "50f25270-9083-4e99-ae16-3ebd172bf89c",
        "UnitID": 0,
        "Password": "2dace9889aaa987ba1975d76b90eaed5cfa28d3d7337c83df56028d76e0359ba;hmacsha256",
        "Id": 100049,
        "Description": "测试"
    }
}
```

