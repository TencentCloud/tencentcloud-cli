**Example 1: 查询专有集群配置列表**

查询专用集群订单配置列表。

Input: 

```
tccli cdc DescribeDedicatedClusterTypes --cli-unfold-argument  \
    --Name abc \
    --DedicatedClusterTypeIds abc \
    --Offset 0 \
    --Limit 10 \
    --IsCompute True
```

Output: 
```
{
    "Response": {
        "DedicatedClusterTypeSet": [
            {
                "DedicatedClusterTypeId": "dctype-lkm17jbu",
                "Description": "first type",
                "Name": "yuan dedicated",
                "CreateTime": "2020-12-16T06:21:41Z",
                "SupportedStorageType": [],
                "SupportedUplinkGiB": [
                    40,
                    100
                ],
                "SupportedInstanceFamily": [
                    "S5"
                ],
                "Weight": 3000,
                "PowerDrawKva": "2000.800000",
                "ComputeFormatDesc": "M5.21XLARGE700 4、S5.21XLARGE320 2"
            },
            {
                "DedicatedClusterTypeId": "dctype-1yo16f1a",
                "Description": "seco type",
                "Name": "abc dedicated",
                "CreateTime": "2020-12-16T06:33:49Z",
                "SupportedStorageType": [],
                "SupportedUplinkGiB": [
                    13,
                    100
                ],
                "SupportedInstanceFamily": [
                    "S1",
                    "S5"
                ],
                "Weight": 3273,
                "PowerDrawKva": "4156.700000",
                "ComputeFormatDesc": "M5.21XLARGE700 4、S5.21XLARGE320 2"
            },
            {
                "DedicatedClusterTypeId": "dctype-b38d7sl6",
                "Description": "heynew",
                "Name": "type und",
                "CreateTime": "2020-12-16T06:33:49Z",
                "SupportedStorageType": [],
                "SupportedUplinkGiB": [
                    10,
                    40
                ],
                "SupportedInstanceFamily": [
                    "S3"
                ],
                "Weight": 3724,
                "PowerDrawKva": "3829.100000",
                "ComputeFormatDesc": "M5.21XLARGE700 4、S5.21XLARGE320 2"
            },
            {
                "DedicatedClusterTypeId": "dctype-z387eu8j",
                "Description": "third one",
                "Name": "unknow",
                "CreateTime": "2020-12-16T06:33:49Z",
                "SupportedStorageType": [],
                "SupportedUplinkGiB": [
                    10,
                    40
                ],
                "SupportedInstanceFamily": [],
                "Weight": 3724,
                "PowerDrawKva": "3829.100000",
                "ComputeFormatDesc": "M5.21XLARGE700 4、S5.21XLARGE320 2"
            }
        ],
        "TotalCount": 4,
        "RequestId": "66221c03-1429-4b8b-b66a-dffa2771536e"
    }
}
```

