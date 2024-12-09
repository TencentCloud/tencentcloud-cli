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
        "TotalCount": 1,
        "InstanceSet": [
            {
                "CcnId": "ccn-ch28gexx",
                "InstanceType": "VPC",
                "InstanceId": "vpc-ch28gexx",
                "InstanceName": "instance-name",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "1234611233",
                "CidrBlock": [
                    "10.0.0.0/24"
                ],
                "State": "ACTIVE",
                "AttachedTime": "2020-09-22 00:00:00",
                "CcnUin": "1234611233",
                "InstanceArea": "CHINA_MAINLAND",
                "Description": "desc",
                "RouteTableId": "ccnr-xxxxxxxx",
                "RouteTableName": "ccnr-name"
            }
        ],
        "RequestId": "0227fa04-3298-470c-8477-149f309a386a"
    }
}
```

