**Example 1: 获取慢查询记录**



Input: 

```
tccli sqlserver DescribeSlowlogs --cli-unfold-argument  \
    --InstanceId mssql-9aajrcn7 \
    --StartTime '2018-03-28 00:00:00' \
    --EndTime '2020-11-20 00:00:00' \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3e166da0-1f64-11eb-98ec-533fb32c3b2c",
        "SlowLogs": [
            {
                "Count": 5,
                "EndTime": "2020-11-05 20:17:14",
                "ExternalAddr": "https://sqlserver-bucket-gz-1258415541.cos.ap-guangzhou.myqcloud.com/1251966477%2fsqlserver%2fmssql-9aajrcn7%2fslow%2fTRACE_20201105201000.trc?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDrRloa5Zdk580Xo9dCWaNE3kU3MQElsiV%26q-sign-time%3d1604580096%3b1604580996%26q-key-time%3d1604580096%3b1604580996%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3d583b4db2ec94fa10e55da9b95e1e3d8943eaa386",
                "Id": 30304577,
                "InternalAddr": "https://sqlserver-bucket-gz-1258415541.cos.ap-guangzhou.myqcloud.com/1251966477%2fsqlserver%2fmssql-9aajrcn7%2fslow%2fTRACE_20201105201000.trc?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDrRloa5Zdk580Xo9dCWaNE3kU3MQElsiV%26q-sign-time%3d1604580096%3b1604580996%26q-key-time%3d1604580096%3b1604580996%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3d583b4db2ec94fa10e55da9b95e1e3d8943eaa386",
                "Size": 1024,
                "StartTime": "2020-11-05 20:10:05",
                "Status": 1
            }
        ],
        "TotalCount": 1
    }
}
```

