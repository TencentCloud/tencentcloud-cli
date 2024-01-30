**Example 1: 获取IP归属**

{
  "Address": [
    "0.0.0.1"
  ]
}

Input: 

```
tccli igtm DescribeAddressLocation --cli-unfold-argument  \
    --Address abc
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
        "RequestId": "abc"
    }
}
```

