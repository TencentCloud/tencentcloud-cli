**Example 1: 查询可用性事件列表**

查询2023年6月9日发生在广州和上海地域的所有云产品可用性事件

Input: 

```
tccli tchd DescribeEvents --cli-unfold-argument  \
    --ProductIds cvm \
    --RegionIds ap-guangzhou ap-shanghai \
    --EventDate 2023-06-09
```

Output: 
```
{
    "Response": {
        "Data": {
            "EventList": [
                {
                    "ProductId": "cvm",
                    "ProductName": "云服务器",
                    "RegionId": "ap-chongqing",
                    "RegionName": "重庆",
                    "StartTime": "2023-06-09 14:16:00",
                    "EndTime": "2023-06-09 14:28:00",
                    "CurrentStatus": "正常"
                }
            ]
        },
        "RequestId": "76a0ee91-c081-4a9c-9ba6-ad7e15f06ce4"
    }
}
```

