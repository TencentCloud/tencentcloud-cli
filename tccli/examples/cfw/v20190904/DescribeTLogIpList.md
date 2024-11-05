**Example 1: DescribeTLogIpList告警中心IP柱形图**

DescribeTLogIpList告警中心IP柱形图

Input: 

```
tccli cfw DescribeTLogIpList --cli-unfold-argument  \
    --EndTime 2024-10-31 15:06:18 \
    --QueryType 1 \
    --SearchValue {"instance_id":"ins-id"} \
    --StartTime 2024-10-01 15:06:18 \
    --Top 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "2001:0db8:3c4d:0015:0000:0000:1a2f:aaaa",
                "Num": 1000,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.163.253",
                "Num": 703,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.166.142",
                "Num": 683,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.166.123",
                "Num": 660,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.167.200",
                "Num": 466,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.167.166",
                "Num": 427,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.162.87",
                "Num": 424,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.162.158",
                "Num": 366,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "129.211.166.134",
                "Num": 366,
                "Port": "80"
            },
            {
                "Address": "广东省深圳市",
                "InsID": "ins-05b5fbe",
                "InsName": "内部服务",
                "Ip": "44.202.62.73",
                "Num": 322,
                "Port": "80"
            }
        ],
        "RequestId": "ca4f0361-bbfd-4935-bf0b-16cf161c2427"
    }
}
```

