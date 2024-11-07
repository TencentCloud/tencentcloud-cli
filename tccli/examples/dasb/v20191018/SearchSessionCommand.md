**Example 1: 命令检索**

命令检索

Input: 

```
tccli dasb SearchSessionCommand --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Cmd pwd \
    --StartTime 2020-01-01T01:01:01+08:00 \
    --EndTime 2020-01-01T01:01:01+08:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CommandSessionSet": [
            {
                "StartTime": "2023-10-04T12:13:45+08:00",
                "EndTime": "2023-10-05T12:13:45+08:00",
                "UserName": "nick",
                "RealName": "roll",
                "DeviceName": "linux",
                "PrivateIp": "10.42.15.13",
                "PublicIp": "172.45.85.62",
                "Commands": [
                    {
                        "Cmd": "rm -rf",
                        "Time": "2023-10-04T12:15:45+08:00",
                        "TimeOffset": 1,
                        "Action": 0,
                        "Sid": "adsasd-asfasd-aswasa",
                        "UserName": "nick",
                        "Account": "root",
                        "InstanceId": "ins-eaaasdsdaw",
                        "FromIp": "10.14.13.52",
                        "SessionTime": "2023-10-05T11:13:45+08:00",
                        "SessTime": "2023-10-05T11:13:45+08:00",
                        "ConfirmTime": "2023-10-05T11:14:45+08:00",
                        "UserDepartmentId": "1",
                        "UserDepartmentName": "总部",
                        "DeviceDepartmentId": "1",
                        "DeviceDepartmentName": "总部",
                        "Size": 1
                    }
                ],
                "Count": 1,
                "Id": "adsasd-asfasd-aswasa",
                "InstanceId": "ins-wafafswafdas",
                "ApCode": "ap-guangzhou-3"
            }
        ],
        "RequestId": "27d70f6b-3732-4698-a00f-ee91d3a1fb3"
    }
}
```

