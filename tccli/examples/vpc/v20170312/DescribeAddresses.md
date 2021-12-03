**Example 1: 查询弹性公网EIP**



Input: 

```
tccli vpc DescribeAddresses --cli-unfold-argument  \
    --AddressIds eip-hxlqja90
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
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

**Example 2: 查询普通公网IP**



Input: 

```
tccli vpc DescribeAddresses --cli-unfold-argument  \
    --Filters.0.Name address-type \
    --Filters.0.Values WanIP
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AddressSet": [
            {
                "AddressId": "eip-7fid2cge",
                "AddressName": null,
                "AddressIp": "43.132.1.131",
                "AddressStatus": "BIND",
                "AddressType": "WanIP",
                "InstanceId": "ins-ywxt3tlk",
                "NetworkInterfaceId": "eni-hrw4cw93",
                "PrivateAddressIp": "172.16.0.103",
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": false,
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "LocalBgp": false,
                "CascadeRelease": false,
                "CreatedTime": "2021-07-30T07:15:47Z",
                "TagSet": [],
                "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                "Bandwidth": 10,
                "InternetServiceProvider": "BGP"
            }
        ],
        "RequestId": "2f73635c-6d4d-4f83-8cc5-48d952fbe04b"
    }
}
```

