**Example 1: 我预定的域名-预约详情**

我预定的域名-预约详情

Input: 

```
tccli domain DescribeBiddingAppointDetail --cli-unfold-argument  \
    --BusinessID xxxx
```

Output: 
```
{
    "Response": {
        "AppointBondPrice": 70,
        "AppointEndTime": "2023-10-28 09:53:48",
        "AppointNum": 1,
        "AppointPrice": 105,
        "AppointStartTime": "2023-10-18 09:53:48",
        "DeleteTime": "2023-11-28 09:53:48",
        "Domain": "sasdfzcccc2216.com",
        "ExpireTime": "2023-09-28 09:53:48",
        "RegTime": "2022-09-28 09:53:48",
        "RequestId": "e0d60073-3fbb-4216-ba20-7ccad80d030a",
        "Status": 7
    }
}
```

