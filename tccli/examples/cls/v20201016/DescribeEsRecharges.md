**Example 1: 获取es导入任务配置列表**



Input: 

```
tccli cls DescribeEsRecharges --cli-unfold-argument  \
    --TopicId 6fd86d3d-705c-4f10-a901-0b32e8a50262 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "CreateTime": 1747203160,
                "EsInfo": {
                    "AccessMode": 1,
                    "Address": "127.0.0.1",
                    "EsType": 2,
                    "Port": 9200,
                    "User": "es_user",
                    "VirtualGatewayType": 0,
                    "VpcId": "vpc-k1xxx0px"
                },
                "ImportInfo": {
                    "EndTime": 1747203035,
                    "StartTime": 1746079835,
                    "Type": 1
                },
                "Index": "my-index-000001",
                "Name": "tt3",
                "Progress": 100,
                "Query": "",
                "Status": 3,
                "SubUin": 100019612237,
                "TaskId": "2de853ac-56ee-4584-8bc2-00876203172e",
                "TimeInfo": {
                    "TimeFormat": "%Y%m%d%H%M%S",
                    "TimeKey": "date",
                    "TimeZone": "UTC+08:00",
                    "Type": 2
                },
                "TopicId": "6fd86d3d-705c-4f10-a901-0b32e8a50262",
                "Uin": 100001127589,
                "UpdateTime": 1747203284
            }
        ],
        "RequestId": "37615831-40b0-44bf-b402-03d71df4c7cb",
        "TotalCount": 4
    }
}
```

