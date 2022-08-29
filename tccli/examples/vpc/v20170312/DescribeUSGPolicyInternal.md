**Example 1: demo**



Input: 

```
tccli vpc DescribeUSGPolicyInternal --cli-unfold-argument  \
    --GetUSGPolicyRequest.0.UsgId sg-5q4brrmt
```

Output: 
```
{
    "Response": {
        "USGPolicySet": [
            {
                "UsgId": "sg-5q4brrmt",
                "ErrorCode": 0,
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "ServiceModule": "ppm-ni1v9ozg",
                        "Id": "sg-e5qrs5d9"
                    },
                    {
                        "Action": "ACCEPT",
                        "ServiceModule": "ppmg-necqdtow",
                        "AddressModule": "ipmg-liaueln6"
                    },
                    {
                        "Ip": "10.0.0.0/8",
                        "Action": "ACCEPT",
                        "ServiceModule": "ppm-rj2pjaz4",
                        "Desc": "test"
                    },
                    {
                        "Ip": "0.0.0.0/0",
                        "Action": "ACCEPT",
                        "Port": "80"
                    }
                ],
                "Outbound": [
                    {
                        "Action": "ACCEPT",
                        "ServiceModule": "ppmg-jyb8z7o4",
                        "Id": "sg-e5qrs5d9"
                    },
                    {
                        "Action": "ACCEPT",
                        "ServiceModule": "ppm-5xfsih5i",
                        "AddressModule": "ipm-4yl03a0s"
                    },
                    {
                        "Action": "ACCEPT",
                        "Ip": "10.0.0.0/8",
                        "ServiceModule": "ppm-rj2pjaz4"
                    },
                    {
                        "Ip": "0.0.0.0/0",
                        "Action": "ACCEPT",
                        "Port": "3389",
                        "Desc": "Windows登陆(3389)"
                    },
                    {
                        "Ip": "0.0.0.0/0",
                        "Action": "ACCEPT",
                        "Port": "22",
                        "Desc": "Linux登陆(22)"
                    }
                ],
                "Version": 17
            }
        ],
        "RequestId": "f2d132b3-d893-496e-b8b3-a9dedcbfc739"
    }
}
```

