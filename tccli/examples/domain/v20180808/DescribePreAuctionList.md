**Example 1: 请求成功示例**

竞价列表

Input: 

```
tccli domain DescribePreAuctionList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PreAuctionList": [
            {
                "BidCount": 2,
                "BiddingTime": "2023-12-23 11:15:05",
                "BusinessId": "P0011702999097821031",
                "Domain": "test-buy-003.com.cn",
                "Op": "noAction",
                "Price": 500
            }
        ],
        "RequestId": "ff5583d9-bd93-444e-b252-3b36f28e0a67",
        "TotalCount": 1
    }
}
```

