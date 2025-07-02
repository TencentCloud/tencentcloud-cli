**Example 1: 查询EIP信息**



Input: 

```
tccli vpc DescribeEipInfos --cli-unfold-argument  \
    --AddressIps 1.14.57.146
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            {
                "AddressId": "eip-gud9dg5i",
                "AddressIp": "193.112.244.148",
                "AddressGroup": "ap-guangzhou",
                "PrivateAddressIp": "172.16.16.17",
                "Region": "ap-guangzhou",
                "Uin": "100005643178",
                "UserUin": "100005643178",
                "InstanceId": "ins-p8et7u8w",
                "LighthouseId": null,
                "CreateTime": "2020-04-21 10:05:10",
                "InstanceType": "CVM"
            }
        ],
        "RequestId": "e637f946-f2e7-4a4c-a2f3-0b9eb2c28902"
    }
}
```

