**Example 1: 请求成功示例**

成功示例

Input: 

```
tccli domain DescribeReservedBidInfo --cli-unfold-argument  \
    --BusinessId P0011712825815133328
```

Output: 
```
{
    "Response": {
        "BidEndTime": "2024-04-11 18:00:00",
        "BidList": [
            {
                "BidStatus": "up",
                "BidTime": "2024-04-11 17:47:45",
                "Price": 2542,
                "User": "155***@qq.com"
            },
            {
                "BidStatus": "down",
                "BidTime": "2024-04-11 17:47:41",
                "Price": 254,
                "User": "155***@qq.com"
            },
            {
                "BidStatus": "down",
                "BidTime": "2024-04-11 17:47:34",
                "Price": 220,
                "User": "155***@qq.com"
            },
            {
                "BidStatus": "down",
                "BidTime": "2024-04-11 17:46:48",
                "Price": 200,
                "User": "roy***@tencent.com"
            },
            {
                "BidStatus": "down",
                "BidTime": "2024-04-11 17:46:38",
                "Price": 180,
                "User": "roy***@tencent.com"
            }
        ],
        "IsUp": true,
        "NextPrice": 2552,
        "Price": 2542,
        "RequestId": "a30e8a24-959c-43e3-a845-63772405b4eb",
        "Status": 2,
        "UpPrice": 2542,
        "UpUser": "155***@qq.com"
    }
}
```

