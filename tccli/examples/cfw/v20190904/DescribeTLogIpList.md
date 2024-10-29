**Example 1: DescribeTLogIpList告警中心IP柱形图**



Input: 

```
tccli cfw DescribeTLogIpList --cli-unfold-argument  \
    --StartTime 2024-10-14 17:06:30 \
    --EndTime 2024-10-21 17:06:30 \
    --Top 10 \
    --QueryType 1 \
    --SearchValue {"instance_id":""}
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Num": 340,
                "Port": "",
                "Address": "",
                "Ip": "129.211.163.253",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 292,
                "Port": "",
                "Address": "",
                "Ip": "129.211.166.142",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 226,
                "Port": "",
                "Address": "",
                "Ip": "129.211.166.123",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 177,
                "Port": "",
                "Address": "",
                "Ip": "129.211.167.200",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 152,
                "Port": "",
                "Address": "",
                "Ip": "129.211.162.158",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 137,
                "Port": "",
                "Address": "",
                "Ip": "129.211.162.87",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 128,
                "Port": "",
                "Address": "",
                "Ip": "129.211.167.166",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 125,
                "Port": "",
                "Address": "",
                "Ip": "129.211.166.134",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 87,
                "Port": "",
                "Address": "",
                "Ip": "103.216.220.22",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 82,
                "Port": "",
                "Address": "",
                "Ip": "129.211.162.23",
                "InsID": "",
                "InsName": ""
            }
        ],
        "RequestId": "0fd1c929-ef54-40d5-b2be-24ebc7296490"
    }
}
```

