**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDirectRoutingList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "IPMask": "255.255.128.0/17",
                    "CreateTime": "2022-12-09T16:43:27+08:00",
                    "IPAddress": "192.168.0.1",
                    "Id": 3,
                    "IPSegment": "192.168.0.0-192.168.127.255"
                },
                {
                    "IPMask": "128.0.0.0/1",
                    "CreateTime": "2022-11-28T20:12:50+08:00",
                    "IPAddress": "10.0.0.1",
                    "Id": 2,
                    "IPSegment": "0.0.0.0-127.255.255.255"
                }
            ]
        },
        "RequestId": "8c6d4c4d-16a2-4a13-b16c-85b04d57d957"
    }
}
```

