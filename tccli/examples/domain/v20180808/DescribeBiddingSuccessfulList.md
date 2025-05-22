**Example 1: 我得标的域名**

我得标的域名

Input: 

```
tccli domain DescribeBiddingSuccessfulList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "340187d9-be66-43e7-a837-80049dad20ec",
        "SuccessfulList": [
            {
                "PayEndTime": "2023-12-25 16:00:00"
            }
        ],
        "Total": 1
    }
}
```

