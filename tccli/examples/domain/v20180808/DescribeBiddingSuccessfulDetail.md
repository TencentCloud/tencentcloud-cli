**Example 1: 我得标的域名-得标详情**

我得标的域名-得标详情

Input: 

```
tccli domain DescribeBiddingSuccessfulDetail --cli-unfold-argument  \
    --BusinessID xxxx
```

Output: 
```
{
    "Response": {
        "BiddingBondPrice": 80,
        "BiddingBondRefund": "no",
        "DeleteTime": "2023-11-28 09:53:48",
        "Domain": "sasdfzcccc2216.com",
        "ExpireTime": "2023-09-28 09:53:48",
        "PayEndTime": "2023-11-07 09:53:48",
        "RegTime": "2022-09-28 09:53:48",
        "RequestId": "7a179528-6d80-495b-8e6c-14b935eccec9",
        "Status": 5,
        "SuccessfulPrice": 200,
        "SuccessfulTime": "2023-10-25 16:00:00"
    }
}
```

