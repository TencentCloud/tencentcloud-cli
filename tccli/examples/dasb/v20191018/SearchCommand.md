**Example 1: 命令执行检索**

命令执行检索

Input: 

```
tccli dasb SearchCommand --cli-unfold-argument  \
    --UserName ac \
    --DeviceName abc \
    --RealName abc \
    --InstanceId asl123 \
    --Cmd abc \
    --AuditAction 1 \
    --PrivateIp 1.1.1.1 \
    --PublicIp 2.2.2.2 \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Offset 1 \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Commands": [
            {
                "UserName": "abc",
                "DeviceName": "ab",
                "RealName": "cc",
                "InstanceId": "abc123",
                "Cmd": "rm",
                "PrivateIp": "1.1.1.1",
                "PublicIp": "2.2.2.2",
                "TimeOffset": 1,
                "Sid": "123",
                "Time": "2020-09-22T00:00:00+00:00",
                "Action": 1
            }
        ],
        "RequestId": "x123456x"
    }
}
```

