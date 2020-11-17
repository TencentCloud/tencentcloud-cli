**Example 1: DescribeSmsSignList**



Input: 

```
tccli zj DescribeSmsSignList --cli-unfold-argument  \
    --License KA3431QZPU \
    --SignIdSet 1110 1111 \
    --International 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "SignId": 1110,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "SignName": "xxx",
                "CreateTime": "2020-01-13 15:18:20"
            },
            {
                "SignId": 1111,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "SignName": "xxx",
                "CreateTime": "2020-01-13 15:18:21"
            }
        ],
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

