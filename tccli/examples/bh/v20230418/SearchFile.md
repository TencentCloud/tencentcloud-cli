**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli bh SearchFile --cli-unfold-argument  \
    --UserName Matthew \
    --DeviceName 测试机 \
    --RealName Noah \
    --PrivateIp 10.12.14.13 \
    --InstanceId ins-ewadwe123 \
    --AuditAction 0 \
    --FileName 12.txt \
    --PublicIp 192.41.15.78 \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Offset 1 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Method 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Files": [
            {
                "Time": "2020-09-22T00:00:00+00:00",
                "UserName": "Leo",
                "RealName": "Hunter",
                "InstanceId": "ins-saew",
                "DeviceName": "测试机",
                "PublicIp": "192.17.13.45",
                "PrivateIp": "127.0.0.1",
                "Action": 1,
                "Method": 1,
                "FileCurr": "1.txt",
                "FileNew": "2.txt"
            }
        ],
        "RequestId": "27d70f6b-3732-4698-a00f-ee91d3a1fb31"
    }
}
```

