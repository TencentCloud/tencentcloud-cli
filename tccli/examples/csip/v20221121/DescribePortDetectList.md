**Example 1: 端口探测列表**

端口探测列表

Input: 

```
tccli csip DescribePortDetectList --cli-unfold-argument  \
    --ExposureID 2147483829 \
    --MemberId None \
    --Limit None \
    --Offset None
```

Output: 
```
{
    "Response": {
        "PortDetectList": [
            {
                "Host": "xx.xx.xx.xx",
                "Port": 22,
                "Protocol": "tcp",
                "Status": "open",
                "UpdateTime": "2025-08-05 19:56:42"
            }
        ],
        "RequestId": "05d75b61-2fa6-4a49-8aaf-2304506f651a",
        "TotalCount": 1
    }
}
```

