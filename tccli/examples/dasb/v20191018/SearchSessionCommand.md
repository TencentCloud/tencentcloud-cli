**Example 1: 命令检索**

命令检索

Input: 

```
tccli dasb SearchSessionCommand --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Cmd pwd \
    --StartTime 2020-01-01T01:01:01Z \
    --EndTime 2020-01-01T01:01:01Z
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CommandSessionSet": [
            {
                "UserName": "xx",
                "DeviceName": "xx",
                "Commands": [
                    {
                        "TimeOffset": 1,
                        "Action": 0,
                        "Cmd": "xx",
                        "Time": "xx"
                    }
                ],
                "RealName": "xx",
                "InstanceId": "xx",
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "Count": 1,
                "StartTime": "xx",
                "EndTime": "xx",
                "Id": "xx",
                "ApCode": "ap-guangzhou"
            }
        ],
        "RequestId": "xx"
    }
}
```

