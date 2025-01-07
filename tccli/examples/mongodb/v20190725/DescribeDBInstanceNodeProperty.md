**Example 1: 查询实例节点信息**

查询实例节点详细属性

Input: 

```
tccli mongodb DescribeDBInstanceNodeProperty --cli-unfold-argument  \
    --InstanceId cmgo-by909vwp
```

Output: 
```
{
    "Response": {
        "Mongos": [
            {
                "Address": "10.8.16.37:30000",
                "Hidden": false,
                "NodeName": "mongos-0",
                "Priority": 0,
                "ReplicateSetId": "",
                "Role": "MONGOS",
                "SlaveDelay": 0,
                "Status": "NORMAL",
                "Tags": [
                    {
                        "TagKey": "role-cmgo",
                        "TagValue": "primary-secondary-group"
                    }
                ],
                "Votes": 0,
                "Zone": "ap-guangzhou-3",
                "WanServiceAddress": ""
            }
        ],
        "ReplicateSets": [
            {
                "Nodes": [
                    {
                        "Address": "",
                        "Hidden": false,
                        "NodeName": "cmgo-by909vwp_0-node-slave0",
                        "Priority": 1,
                        "ReplicateSetId": "cmgo-by909vwp_0",
                        "Role": "SECONDARY",
                        "SlaveDelay": 0,
                        "Status": "NORMAL",
                        "WanServiceAddress": "",
                        "Tags": [
                            {
                                "TagKey": "role-cmgo",
                                "TagValue": "primary-secondary-group"
                            }
                        ],
                        "Votes": 1,
                        "Zone": "ap-guangzhou-3"
                    }
                ]
            },
            {
                "Nodes": [
                    {
                        "Address": "",
                        "Hidden": false,
                        "NodeName": "cmgo-by909vwp_1-node-slave0",
                        "Priority": 1,
                        "ReplicateSetId": "cmgo-by909vwp_1",
                        "Role": "SECONDARY",
                        "SlaveDelay": 0,
                        "Status": "NORMAL",
                        "WanServiceAddress": "",
                        "Tags": [
                            {
                                "TagKey": "role-cmgo",
                                "TagValue": "primary-secondary-group"
                            }
                        ],
                        "Votes": 1,
                        "Zone": "ap-guangzhou-3"
                    },
                    {
                        "Address": "",
                        "Hidden": false,
                        "NodeName": "cmgo-by909vwp_1-node-primary",
                        "Priority": 1,
                        "ReplicateSetId": "cmgo-by909vwp_1",
                        "Role": "PRIMARY",
                        "SlaveDelay": 0,
                        "Status": "NORMAL",
                        "WanServiceAddress": "",
                        "Tags": [
                            {
                                "TagKey": "role-cmgo",
                                "TagValue": "primary-secondary-group"
                            }
                        ],
                        "Votes": 1,
                        "Zone": "ap-guangzhou-3"
                    },
                    {
                        "Address": "",
                        "Hidden": true,
                        "NodeName": "cmgo-by909vwp_1-node-slave1",
                        "Priority": 0,
                        "ReplicateSetId": "cmgo-by909vwp_1",
                        "Role": "SECONDARY",
                        "SlaveDelay": 0,
                        "Status": "NORMAL",
                        "WanServiceAddress": "",
                        "Tags": [
                            {
                                "TagKey": "role-cmgo",
                                "TagValue": "primary-secondary-group"
                            }
                        ],
                        "Votes": 1,
                        "Zone": "ap-guangzhou-3"
                    }
                ]
            }
        ],
        "RequestId": "14ab088a-9d69-44b4-b39d-e4b8fbbb8f25"
    }
}
```

