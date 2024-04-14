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
        "BidList": [
            {
                "BidStatus": "up",
                "BidTime": "17:19:30",
                "Price": 210,
                "User": "roy***@tencent.com"
            },
            {
                "BidStatus": "down",
                "BidTime": "17:18:45",
                "Price": 200,
                "User": "155***@qq.com"
            },
            {
                "BidStatus": "down",
                "BidTime": "17:15:24",
                "Price": 190,
                "User": "roy***@tencent.com"
            }
        ],
        "Price": 200,
        "RequestId": "43271422-1fe8-4af5-99ff-afc140ea35b2",
        "UpPrice": 210,
        "UpUser": "roy***@tencent.com"
    }
}
```

