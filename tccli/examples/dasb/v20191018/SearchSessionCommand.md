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
                "UserName": "aa",
                "DeviceName": "aa",
                "Commands": [
                    {
                        "TimeOffset": 1,
                        "Action": 0,
                        "Cmd": "cd",
                        "Time": "2020-01-01T01:01:01Z"
                    }
                ],
                "RealName": "aa",
                "InstanceId": "aa",
                "PrivateIp": "aa",
                "PublicIp": "aa",
                "Count": 1,
                "StartTime": "2020-01-01T01:01:01Z",
                "EndTime": "2020-01-01T01:01:01Z",
                "Id": "123",
                "ApCode": "ap-guangzhou"
            }
        ],
        "RequestId": "asd123"
    }
}
```

