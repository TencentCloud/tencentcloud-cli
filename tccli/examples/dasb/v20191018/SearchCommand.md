**Example 1: 命令执行检索**

命令执行检索

Input: 

```
tccli dasb SearchCommand --cli-unfold-argument  \
    --UserName jack \
    --DeviceName test-name \
    --RealName test-name \
    --InstanceId ins-asl123 \
    --Cmd pwd \
    --AuditAction 1 \
    --PrivateIp 1.1.1.1 \
    --PublicIp 2.2.2.2 \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+08:00 \
    --Offset 1 \
    --EndTime 2020-09-22T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Commands": [
            {
                "UserName": "Charlotte",
                "DeviceName": "开发机",
                "RealName": "nick",
                "UserDepartmentId": "1",
                "DeviceDepartmentId": "1",
                "UserDepartmentName": "总部",
                "DeviceDepartmentName": "总部",
                "InstanceId": "ins-1weqqere",
                "Cmd": "rm",
                "PrivateIp": "1.1.1.1",
                "PublicIp": "2.2.2.2",
                "TimeOffset": 1,
                "Account": "root",
                "FromIp": "192.168.0.1",
                "Sid": "wewqew-21dw-wwedfsf",
                "SessTime": "2020-09-22T00:00:00+08:00",
                "ConfirmTime": "2020-09-22T00:00:00+08:00",
                "Time": "2020-09-22T00:00:00+08:00",
                "Action": 1
            }
        ],
        "RequestId": "aa23ab6a-b9ed-41b2-8fa3-7ab59d3e0b47"
    }
}
```

