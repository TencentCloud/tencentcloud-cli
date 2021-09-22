**Example 1: 使用AddressIds查询EIP**



Input: 

```
tccli vpc DescribeAddresses --cli-unfold-argument  \
    --AddressIds eip-hxlqja90
```

Output: 
```
{
    "Response": {
        "TotalCount": 385,
        "AddressSet": [
            {
                "AddressId": "eip-76w7384s",
                "AddressName": null,
                "AddressIp": "106.55.251.58",
                "AddressStatus": "UNBIND",
                "AddressType": "EIP",
                "InstanceId": null,
                "NetworkInterfaceId": null,
                "PrivateAddressIp": null,
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": false,
                "EipAlgType": {
                    "Ftp": false,
                    "Sip": false
                },
                "LocalBgp": false,
                "CascadeRelease": false,
                "CreatedTime": "2020-10-20T08:19:31Z",
                "InternetChargeType": "BANDWIDTH_PACKAGE",
                "Bandwidth": 65535,
                "InternetServiceProvider": "BGP",
                "TagSet": [
                    {
                        "Key": "tag1",
                        "Value": "value1"
                    }
                ]
            },
            {
                "AddressId": "eip-lshmvwlc",
                "AddressName": null,
                "AddressIp": "81.71.146.150",
                "AddressStatus": "UNBIND",
                "AddressType": "EIP",
                "InstanceId": null,
                "NetworkInterfaceId": null,
                "PrivateAddressIp": null,
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": false,
                "EipAlgType": {
                    "Ftp": false,
                    "Sip": false
                },
                "LocalBgp": false,
                "CascadeRelease": false,
                "CreatedTime": "2020-10-20T08:19:29Z",
                "InternetChargeType": "BANDWIDTH_PACKAGE",
                "Bandwidth": 65535,
                "InternetServiceProvider": "BGP",
                "TagSet": [
                    {
                        "Key": "tag2",
                        "Value": "value2"
                    }
                ]
            }
        ],
        "RequestId": "42bc5893-70ff-4f13-bcc3-1308dedab8f6"
    }
}
```

