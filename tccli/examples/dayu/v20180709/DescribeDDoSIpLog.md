**Example 1: Getting DDoS IP attack log**



Input: 

```
tccli dayu DescribeDDoSIpLog --cli-unfold-argument  \
    --Business net\
    --Id net-00000010\
    --IpList 1.1.1.1\
    --StartTime '2018-08-27 15:05:10'\
    --EndTime '2018-08-27 16:05:10'
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "Id": "net-00000010",
        "Ip": "3.3.1.6",
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
                        "Value": "3.3.1.6 (Shanghai, China Unicom) is under DDoS attack with an attack traffic bandwidth of 10,123 Mbps"
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
                        "Value": "The DDoS attack to 3.3.1.6 (Shanghai, China Unicom) has stopped"
                    }
                ]
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

