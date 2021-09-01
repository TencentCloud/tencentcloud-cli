**Example 1: 获取高防IP专业版资源的DDoSIP攻击日志**



Input: 

```
tccli dayu DescribeDDoSNetIpLog --cli-unfold-argument  \
    --Business net \
    --Id net-00000010 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10'
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "Id": "net-00000010",
        "StartTime": "2019-03-06 09:32:00",
        "EndTime": "2019-03-06 09:48:00",
        "Data": [
            {
                "Record": [
                    {
                        "Key": "LogTime",
                        "Value": "2019-03-12 10:35:15"
                    },
                    {
                        "Key": "LogMessage",
                        "Value": "3.3.1.6(上海, 联通)受到DDoS攻击, 攻击流量达10123Mbps"
                    }
                ]
            },
            {
                "Record": [
                    {
                        "Key": "LogTime",
                        "Value": "2019-03-12 10:35:05"
                    },
                    {
                        "Key": "LogMessage",
                        "Value": "3.3.1.6(上海, 联通)遭受的DDoS攻击已停止"
                    }
                ]
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

