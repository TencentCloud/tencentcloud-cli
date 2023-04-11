**Example 1: 搜索session列表**

搜索session列表

Input: 

```
tccli dasb SearchFile --cli-unfold-argument  \
    --UserName xx \
    --DeviceName xx \
    --RealName xx \
    --PrivateIp xx \
    --InstanceId xx \
    --AuditAction 0 \
    --FileName xx \
    --PublicIp xx \
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
        "Files": [
            {
                "UserName": "xx",
                "DeviceName": "xx",
                "RealName": "xx",
                "InstanceId": "xx",
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "Time": "xx",
                "Action": 1,
                "Method": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

