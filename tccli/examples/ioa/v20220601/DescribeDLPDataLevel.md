**Example 1: 查询数据级别**

查询租户数据级别

Input: 

```
tccli ioa DescribeDLPDataLevel --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Color": "#AAAAAA",
                "Name": "S1",
                "IsReferenced": true,
                "Utime": "2025-08-26T16:48:27.469887Z",
                "Id": 1,
                "Description": "公开级别",
                "Itime": "2025-08-26T16:48:27.469887Z",
                "Status": 1
            },
            {
                "Color": "#FAC335",
                "Name": "S2",
                "IsReferenced": true,
                "Utime": "2025-08-26T16:48:27.469887Z",
                "Id": 2,
                "Description": "内部级别",
                "Itime": "2025-08-26T16:48:27.469887Z",
                "Status": 1
            },
            {
                "Color": "#F4A547",
                "Name": "S3",
                "IsReferenced": true,
                "Utime": "2025-08-26T16:48:27.469887Z",
                "Id": 3,
                "Description": "敏感级别",
                "Itime": "2025-08-26T16:48:27.469887Z",
                "Status": 1
            },
            {
                "Color": "#F37D58",
                "Name": "S4",
                "IsReferenced": true,
                "Utime": "2025-08-26T16:48:27.469887Z",
                "Id": 4,
                "Description": "重要级别",
                "Itime": "2025-08-26T16:48:27.469887Z",
                "Status": 1
            },
            {
                "Color": "#E24C55",
                "Name": "S5",
                "IsReferenced": false,
                "Utime": "2025-08-26T16:48:27.469887Z",
                "Id": 5,
                "Description": "机密级别",
                "Itime": "2025-08-26T16:48:27.469887Z",
                "Status": 0
            },
            {
                "Color": "#A3373D",
                "Name": "S6",
                "IsReferenced": false,
                "Utime": "2025-08-26T16:48:27.469887Z",
                "Id": 6,
                "Description": "绝密级别",
                "Itime": "2025-08-26T16:48:27.469887Z",
                "Status": 0
            }
        ],
        "RequestId": "web-9373221634-1765953832597"
    }
}
```

