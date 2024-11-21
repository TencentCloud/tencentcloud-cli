**Example 1: DescribeBlockStaticList 告警中心柱形图**

DescribeBlockStaticList 告警中心柱形图

Input: 

```
tccli cfw DescribeBlockStaticList --cli-unfold-argument  \
    --EndTime 2024-11-01 14:23:11 \
    --QueryType ip \
    --SearchValue {"instance_id":"ins-id","source":"cvm"} \
    --StartTime 2024-10-25 14:23:11 \
    --Top 5
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Address": "beijing",
                "InsID": "ins-cvmid",
                "InsName": "cvmname",
                "Ip": "141.98.11.67",
                "Num": 39,
                "Port": "22"
            }
        ],
        "RequestId": "7138a2b1-f1fb-4b72-b49d-b8fcaec2afcb",
        "Status": 0
    }
}
```

