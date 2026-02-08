**Example 1: 查询运维子任务执行结果**

查询运维子任务执行结果

Input: 

```
tccli bh SearchSubtaskResultById --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Id 4fda0e7f-6741-401c-a4c1-ca5872097c9c
```

Output: 
```
{
    "Response": {
        "SubtaskResult": [
            {
                "Account": "root",
                "ApCode": "ap-guangzhou",
                "DeviceName": "Centos-7.9",
                "EndTime": "2026-02-05T18:28:38+08:00",
                "ExitCode": 0,
                "Id": "4fda0e7f-6741-401c-a4c1-ca5872097c9c_0",
                "InstanceId": "ins-xxxxxx",
                "Name": "",
                "PrivateIp": "192.168.0.6",
                "PublicIp": "143.156.236.100",
                "Reason": "",
                "StartTime": "2026-02-05T18:28:37+08:00",
                "Status": 2,
                "StdErr": "",
                "StdOut": "hello, world\r\n"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c6f7f69a-1c89-4982-87c4-c954fe10b0cc"
    }
}
```

