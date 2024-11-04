**Example 1: DescribeBlockStaticList**



Input: 

```
tccli cfw DescribeBlockStaticList --cli-unfold-argument  \
    --StartTime 2024-10-14 17:07:36 \
    --EndTime 2024-10-21 17:07:36 \
    --Top 5 \
    --QueryType ip \
    --SearchValue {"instance_id":"","source":""}
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Num": 3145,
                "Port": "",
                "Address": "",
                "Ip": "45.84.89.3",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 3126,
                "Port": "",
                "Address": "",
                "Ip": "45.84.89.2",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 1152,
                "Port": "",
                "Address": "",
                "Ip": "179.43.133.162",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 755,
                "Port": "",
                "Address": "",
                "Ip": "60.191.20.210",
                "InsID": "",
                "InsName": ""
            },
            {
                "Num": 731,
                "Port": "",
                "Address": "",
                "Ip": "185.224.128.67",
                "InsID": "",
                "InsName": ""
            }
        ],
        "RequestId": "a7c543d3-b4b7-437c-9088-f4ab462f28ca",
        "Status": 0
    }
}
```

