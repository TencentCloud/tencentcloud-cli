**Example 1: 我的竞价列表**

我的竞价列表

Input: 

```
tccli domain DescribeBiddingList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "BiddingList": [
            {
                "BiddingBondPrice": 0,
                "BiddingEndTime": "2023-11-04 09:53:48",
                "BiddingFlag": 0,
                "BiddingNum": 1,
                "BiddingPrice": 0,
                "BusinessID": "xxxx",
                "CurrentNickname": "feng",
                "CurrentPrice": 120,
                "Domain": "sasdfzcccc2216.com",
                "Status": 7
            },
            {
                "BiddingBondPrice": 80,
                "BiddingEndTime": "2023-11-04 09:53:48",
                "BiddingFlag": 1,
                "BiddingNum": 1,
                "BiddingPrice": 150,
                "BusinessID": "xxxx",
                "CurrentNickname": "feng",
                "CurrentPrice": 120,
                "Domain": "sasdfzcccc2216.com",
                "Status": 2
            }
        ],
        "RequestId": "560e00d9-ddf1-4d4b-a3d8-461eb8c8e40c",
        "Total": 2
    }
}
```

