**Example 1: 我的预约列表**

我的预约列表

Input: 

```
tccli domain DescribeBiddingAppointList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "AppointList": [
            {
                "AppointBondPrice": 70,
                "AppointEndTime": "2023-10-28T09:53:48+08:00",
                "AppointNum": 1,
                "AppointPrice": 105,
                "BusinessID": "***561",
                "Domain": "sasdfzcccc2216.com",
                "Status": 1
            }
        ],
        "RequestId": "02f51803-507c-40ad-b26a-9a0178fa7ffc",
        "Total": 1
    }
}
```

