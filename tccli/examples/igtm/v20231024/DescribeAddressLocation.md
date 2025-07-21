**Example 1: 获取IP归属**

{
  "Address": [
    "0.0.0.1"
  ]
}

Input: 

```
tccli igtm DescribeAddressLocation --cli-unfold-argument  \
    --Address 0.0.0.1
```

Output: 
```
{
    "Response": {
        "AddressLocation": [
            {
                "Addr": "0.0.0.1",
                "Location": "未知"
            }
        ],
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

