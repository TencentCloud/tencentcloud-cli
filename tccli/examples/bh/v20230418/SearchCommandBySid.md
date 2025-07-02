**Example 1: 根据会话Id搜索Command**

根据会话Id搜索Command

Input: 

```
tccli bh SearchCommandBySid --cli-unfold-argument  \
    --Sid qee131were2
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "ec7676f4-a498-4ef5-ad68-6678b16e45d7",
        "CommandSet": [
            {
                "Sid": "d6021542-c198-4d6f-a1fd-a8091544847c",
                "UserName": "test-0701",
                "Account": "root",
                "InstanceId": "ins-h8wdh7my",
                "FromIp": "139.199.149.81",
                "SessTime": "2025-07-01T19:25:31.439302203+08:00",
                "SessionTime": "2025-07-01T19:25:31.439302203+08:00",
                "Time": "2025-07-01T19:25:34.393856986+08:00",
                "TimeOffset": 2954,
                "Cmd": "date",
                "Action": 1,
                "UserDepartmentId": "1",
                "UserDepartmentName": "总部",
                "DeviceDepartmentId": "1",
                "DeviceDepartmentName": "总部",
                "DeviceKind": "TKE",
                "SignValue": "690ffb6bc1e1",
                "Size": 1937
            }
        ]
    }
}
```

