**Example 1: 查询EIP信息**

查询EIP信息。

Input: 

```
tccli vpc DescribeAddresses --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "AddressSet": [
            {
                "AddressId": "eip-qhx8udkc",
                "AddressName": "未命名",
                "AddressIp": "1.14.91.34",
                "AddressStatus": "UNBIND",
                "AddressType": "EIP",
                "InstanceId": "ins-wf123456",
                "InstanceType": null,
                "NetworkInterfaceId": "eni-12345678",
                "PrivateAddressIp": "10.2.3.4",
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": false,
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "LocalBgp": false,
                "CascadeRelease": false,
                "CreatedTime": "2022-08-11T03:57:05Z",
                "TagSet": [],
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Bandwidth": 1,
                "DeadlineDate": null,
                "Egress": "center_egress1",
                "InternetServiceProvider": "BGP"
            },
            {
                "AddressId": "eip-qygpzm9y",
                "AddressName": "未命名",
                "AddressIp": "1.14.90.212",
                "AddressStatus": "UNBIND",
                "AddressType": "EIP",
                "InstanceId": "ins-12345678",
                "InstanceType": null,
                "NetworkInterfaceId": "eni-12345678",
                "PrivateAddressIp": "10.3.4.5.6",
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": false,
                "Egress": "center_egress1",
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "LocalBgp": false,
                "CascadeRelease": false,
                "CreatedTime": "2022-08-11T03:47:03Z",
                "TagSet": [],
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Bandwidth": 1,
                "DeadlineDate": null,
                "InternetServiceProvider": "BGP"
            }
        ],
        "RequestId": "4ead34c4-3112-40fe-bbde-2295eee9d664"
    }
}
```

**Example 2: 查询普通公网IP**

查询普通公网IP。

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
                "AddressId": "eip-93gyo275",
                "AddressName": "gwlb",
                "AddressIp": "122.51.235.39",
                "AddressStatus": "BIND",
                "AddressType": "WanIP",
                "InstanceId": "ins-b2mc0ko1",
                "InstanceType": "CVM",
                "NetworkInterfaceId": "eni-akohvkv6",
                "PrivateAddressIp": "10.0.1.9",
                "IsArrears": false,
                "IsBlocked": false,
                "IsEipDirectConnection": false,
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "LocalBgp": false,
                "CascadeRelease": false,
                "Egress": "center_egress1",
                "CreatedTime": "2024-11-11T07:42:49Z",
                "TagSet": [
                    {
                        "Key": "qcs:tag:createdBy",
                        "Value": "Root:100002840660"
                    }
                ],
                "BandwidthPackageId": null,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Bandwidth": 5,
                "DeadlineDate": null,
                "InternetServiceProvider": "BGP"
            }
        ],
        "RequestId": "f9b58176-c138-45ba-a0e2-7a55117e2833"
    }
}
```

**Example 3: 查询弹性公网EIP**

查询弹性公网EIP。

Input: 

```
tccli vpc DescribeAddresses --cli-unfold-argument  \
    --AddressIds eip-hxlqja90
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AddressSet": [
            {
                "AddressId": "eip-12345678",
                "AddressName": "abc",
                "AddressStatus": "UNBIND",
                "AddressIp": "34.3.4.5.6",
                "InstanceId": "ins-12345678",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "NetworkInterfaceId": "eni-12345678",
                "PrivateAddressIp": "10.2.3.4",
                "IsArrears": true,
                "IsBlocked": true,
                "IsEipDirectConnection": true,
                "AddressType": "WanIp",
                "CascadeRelease": true,
                "EipAlgType": {
                    "Ftp": true,
                    "Sip": true
                },
                "InternetServiceProvider": "BGP",
                "LocalBgp": true,
                "Bandwidth": 1,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "TagSet": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "DeadlineDate": "2020-09-22",
                "InstanceType": "abc",
                "Egress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

