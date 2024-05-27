**Example 1: 请求成功示例**

列表数据

Input: 

```
tccli domain DescribePreReleaseList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PreReleaseList": [
            {
                "BusinessId": "P0011703064185349649",
                "CurrentPeople": 1,
                "DelTime": "2024-01-16 00:00:00",
                "Domain": "099hq.net",
                "IsAppoint": false,
                "IsFollow": false,
                "Price": 102,
                "RegTime": "2020-01-01 00:00:00",
                "ReservationTime": "2023-12-31 07:32:05"
            },
            {
                "BusinessId": "P0011703067801554141",
                "CurrentPeople": 1,
                "DelTime": "2024-01-16 00:00:00",
                "Domain": "095hq.net",
                "IsAppoint": false,
                "IsFollow": false,
                "Price": 102,
                "RegTime": "2020-01-01 00:00:00",
                "ReservationTime": "2023-12-31 07:32:05"
            },
            {
                "BusinessId": "P0011702284530637838",
                "CurrentPeople": 2,
                "DelTime": "2024-01-16 00:00:00",
                "Domain": "091hq.net",
                "IsAppoint": false,
                "IsFollow": false,
                "Price": 102,
                "RegTime": "2020-01-01 00:00:00",
                "ReservationTime": "2023-12-31 07:32:05"
            }
        ],
        "RequestId": "543393c3-28c3-4de0-8535-1256fe004410",
        "TotalCount": 3
    }
}
```

