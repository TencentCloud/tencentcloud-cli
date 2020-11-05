**Example 1: Getting Tencent Cloud asset information corresponding to IP of single IP instance or multi-IP instance**



Input: 

```
tccli dayu DescribeIPProductInfo --cli-unfold-argument  \
    --Business bgp\
    --IpList 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "8466d9e1-70a9-4575-8e02-df15bd50bc49",
        "Business": "bgpip",
        "ServicePacks": [
            {
                "Record": [
                    {
                        "Key": "ProductName",
                        "Value": "test"
                    },
                    {
                        "Key": "ProductInstanceId",
                        "Value": "ins-ryv7esb2"
                    },
                    {
                        "Key": "ProductType",
                        "Value": "cvm"
                    },
                    {
                        "Key": "IP",
                        "Value": "1.1.1.1"
                    }
                ]
            }
        ]
    }
}
```

