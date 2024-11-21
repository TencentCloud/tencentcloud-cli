**Example 1: 查询篡改事件列表**



Input: 

```
tccli cwp DescribeWebPageEventList --cli-unfold-argument  \
    --By CreateTime \
    --Order 1 \
    --Filters.0.Name IpOrAlias \
    --Filters.0.Values 'HostName or HostIp'
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostName": "DataHub",
                "HostIp": "1.2.3.4",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "EventDir": "/root/csipdata/virus/php/1.php",
                "EventType": 4,
                "EventStatus": 1,
                "CreateTime": "2024-08-16 11:49:11",
                "RestoreTime": "2024-09-12 18:09:57",
                "Id": 423826,
                "FileType": 0,
                "MachineExtraInfo": {
                    "WanIP": "1.2.3.4",
                    "PrivateIP": "192.168.10.10",
                    "NetworkType": 0,
                    "NetworkName": "name",
                    "InstanceID": "ins-ac13d",
                    "HostName": "dataHub"
                }
            }
        ],
        "RequestId": "d9506441-52bc-4d14-a767-7e1251ed3ced",
        "TotalCount": 1
    }
}
```

