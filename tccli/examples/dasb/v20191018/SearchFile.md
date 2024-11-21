**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli dasb SearchFile --cli-unfold-argument  \
    --UserName Joseph \
    --DeviceName 开发机 \
    --RealName Daniel \
    --PrivateIp 192.10.63.14 \
    --InstanceId ins-wedggutfye \
    --AuditAction 0 \
    --FileName test.txt \
    --PublicIp 192.16.35.36 \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+08:00 \
    --Offset 1 \
    --EndTime 2020-09-22T00:00:00+08:00 \
    --Method 1
```

Output: 
```
{
    "Response": {
        "Files": [
            {
                "UserName": "Andrew",
                "DeviceName": "开发机",
                "RealName": "Benjamin",
                "InstanceId": "ins-aassdds",
                "PrivateIp": "182.64.45.62",
                "PublicIp": "192.45.68.15",
                "Time": "2020-09-22T00:00:00+08:00",
                "Action": 1,
                "Method": 1,
                "FileCurr": "tmp.so",
                "FileNew": "/home/1.txt"
            }
        ],
        "TotalCount": 1,
        "RequestId": "1d3ef406-46bd-4770-8f0b-dbd4ac3d886e"
    }
}
```

