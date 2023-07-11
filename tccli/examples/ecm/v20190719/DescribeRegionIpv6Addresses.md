**Example 1: 根据Ip6AddressIds查询地域下的IPV6信息**



Input: 

```
tccli ecm DescribeRegionIpv6Addresses --cli-unfold-argument  \
    --EcmRegion ap-qingdao-ecm
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-lrhy2lpe",
                "AddressIp": "2402:4e00:1000:2d00:0:8f3f:6:9895",
                "AddressStatus": "BIND",
                "InstanceId": "ein-190087yw",
                "NetworkInterfaceId": "eni-rw4fh3gn",
                "IsArrears": false,
                "CreatedTime": "2020-01-13T04:09:52Z",
                "Bandwidth": 6,
                "IsEipDirectConnection": true,
                "PrivateAddressIp": "",
                "AddressName": "name",
                "PayMode": "0",
                "CascadeRelease": true,
                "InternetServiceProvider": "CTCC",
                "AddressType": "",
                "IsBlocked": true
            }
        ],
        "RequestId": "bfe06911-32f5-4862-9d42-6bb4954dcb59"
    }
}
```

