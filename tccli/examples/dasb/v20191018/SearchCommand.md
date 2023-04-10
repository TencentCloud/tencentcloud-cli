**Example 1: 命令执行检索**

命令执行检索

Input: 

```
tccli dasb SearchCommand --cli-unfold-argument  \
    --UserName xx \
    --DeviceName xx \
    --RealName xx \
    --InstanceId xx \
    --Cmd xx \
    --AuditAction 1 \
    --PrivateIp xx \
    --PublicIp xx \
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
                "UserName": "xx",
                "DeviceName": "xx",
                "RealName": "xx",
                "InstanceId": "xx",
                "Cmd": "xx",
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "TimeOffset": 1,
                "Sid": "xx",
                "Time": "xx",
                "Action": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

