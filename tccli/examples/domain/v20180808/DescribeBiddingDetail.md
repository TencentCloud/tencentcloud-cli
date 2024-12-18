**Example 1: 我竞价的域名-竞价详情**

我竞价的域名-竞价详情

Input: 

```
tccli domain DescribeBiddingDetail --cli-unfold-argument  \
    --BusinessID ***561
```

Output: 
```
{
    "Response": {
        "BiddingBondPrice": 80,
        "BiddingBondRefund": "no",
        "BiddingEndTime": "2023-11-04 09:53:48",
        "BiddingFlag": 1,
        "BiddingNum": 1,
        "BiddingPrice": 150,
        "BiddingStartTime": "2023-10-28 09:53:48",
        "CurrentNickname": "feng",
        "CurrentPrice": 120,
        "DeleteTime": "2023-11-28 09:53:48",
        "Domain": "***16.com",
        "ExpireTime": "2023-09-28 09:53:48",
        "RegTime": "2022-09-28 09:53:48",
        "RequestId": "5fdc5b55-514b-42f8-85a3-e269db61f752",
        "Status": 2
    }
}
```

