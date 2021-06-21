**Example 1: 获取DDoS防护的IP黑白名单**



Input: 

```
tccli antiddos DescribeBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-00001001
```

Output: 
```
{
    "Response": {
        "RequestId": "0f996729-bb5b-49da-89c3-8fc2a7400bd5",
        "BlackIpList": [
            "123.123.123.1"
        ],
        "WhiteIpList": [
            "123.123.123.2"
        ]
    }
}
```

