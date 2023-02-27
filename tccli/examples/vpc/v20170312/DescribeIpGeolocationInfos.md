**Example 1: 查询IP地理位置信息**

查询IP地理位置信息。

Input: 

```
tccli vpc DescribeIpGeolocationInfos --cli-unfold-argument  \
    --AddressIps 8.8.8.8 2001:1200:: \
    --Fields.Province True \
    --Fields.Country True \
    --Fields.Region True \
    --Fields.Isp True \
    --Fields.City True
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "AddressInfo": [
            {
                "AddressIp": "2001:1200::",
                "Country": "墨西哥",
                "Province": "tabasco",
                "City": "miguel hidalgo",
                "Region": "未知",
                "Isp": "protel i-next, s.a. de c.v., mx"
            },
            {
                "AddressIp": "8.8.8.8",
                "Country": "美国",
                "Province": "california",
                "City": "mountain view",
                "Region": "未知",
                "Isp": "google - google inc., us"
            }
        ],
        "RequestId": "6d3e1ba5-a3d0-41d4-93f7-4992a2e18b9d"
    }
}
```

