**Example 1: 查询云联网关联实例列表**

用于查询云联网实例下已关联的网络实例

Input: 

```
tccli vpc DescribeCcnAttachedInstances --cli-unfold-argument  \
    --Filters.0.Values vpc-r1ckkpid vpc-2u0s99fx dcg-98qosdc3 vpc-3dr1zrr9 dcg-ni7ps9kb \
    --Filters.0.Name instance-id \
    --Filters.1.Values ccn-gree226l \
    --Filters.1.Name ccn-id
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "CcnId": "ccn-gree226l",
                "InstanceType": "VPC",
                "InstanceId": "vpc-2u0s99fx",
                "InstanceName": "test1",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "38059483",
                "CidrBlock": [
                    "10.0.0.0/16"
                ],
                "State": "PENDING",
                "CcnUin": "100000072292",
                "InstanceArea": "CHINA_MAINLAND",
                "AttachedTime": "2021-03-03 16:19:44",
                "RouteTableId": null,
                "RouteTableName": null,
                "Description": ""
            },
            {
                "CcnId": "ccn-gree226l",
                "InstanceType": "VPC",
                "InstanceId": "vpc-r1ckkpid",
                "InstanceName": "vpc0420",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "88419914",
                "CidrBlock": [
                    "10.33.0.0/16"
                ],
                "State": "REJECTED",
                "CcnUin": "100000072292",
                "InstanceArea": "CHINA_MAINLAND",
                "AttachedTime": "2021-03-03 16:19:44",
                "RouteTableId": null,
                "RouteTableName": null,
                "Description": ""
            },
            {
                "CcnId": "ccn-gree226l",
                "InstanceType": "VPC",
                "InstanceId": "vpc-3dr1zrr9",
                "InstanceName": "10.100.0.0/16",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "979137",
                "CidrBlock": [
                    "10.100.0.0/16"
                ],
                "State": "ACTIVE",
                "CcnUin": "100000072292",
                "InstanceArea": "CHINA_MAINLAND",
                "AttachedTime": "2021-03-03 16:19:44",
                "RouteTableId": null,
                "RouteTableName": null,
                "Description": ""
            },
            {
                "CcnId": "ccn-gree226l",
                "InstanceType": "DIRECTCONNECT",
                "InstanceId": "dcg-98qosdc3",
                "InstanceName": "",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "979137",
                "CidrBlock": [
                    "192.168.0.0/24"
                ],
                "State": "ACTIVE",
                "CcnUin": "100000072292",
                "InstanceArea": "CHINA_MAINLAND",
                "AttachedTime": "2021-03-03 16:19:44",
                "RouteTableId": null,
                "RouteTableName": null,
                "Description": ""
            },
            {
                "CcnId": "ccn-gree226l",
                "InstanceType": "DIRECTCONNECT",
                "InstanceId": "dcg-ni7ps9kb",
                "InstanceName": "",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "979137",
                "CidrBlock": [
                    "192.168.1.0/24"
                ],
                "State": "ACTIVE",
                "CcnUin": "100000072292",
                "InstanceArea": "CHINA_MAINLAND",
                "AttachedTime": "2021-03-03 16:19:44",
                "RouteTableId": null,
                "RouteTableName": null,
                "Description": ""
            }
        ],
        "TotalCount": 5,
        "RequestId": "0227fa04-3298-470c-8477-149f309a386a"
    }
}
```

