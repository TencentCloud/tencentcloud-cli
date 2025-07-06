**Example 1: 列出 GooseFS 集群**

列出所有的 GooseFS 集群

Input: 

```
tccli goosefs DescribeClusters --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ClusterAttributeList": [
            {
                "ClusterId": "g_cvm_744ikj5x",
                "Name": "MyTestFS",
                "Status": "alive",
                "Type": "goosefs",
                "VpcId": "vpc-123",
                "SubnetId": "subnet-123",
                "Zone": "ap-guangzhou-3",
                "Description": "my test fs",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "Tag": [
                    {
                        "Value": "production",
                        "Key": "env"
                    }
                ],
                "GooseFSAttribute": {
                    "ClusterHighAvailability": "是",
                    "ClusterDeployType": "INDEPENDENT_CLUSTER",
                    "GooseFSCloudAuth": true,
                    "InstanceType": "CVM",
                    "TkeClusterId": "xxx",
                    "ClientNumber": 111,
                    "GooseFSNodeList": [
                        {
                            "NodeIp": "10.0.0.1",
                            "InstanceId": "xxx",
                            "InstanceType": "CVM",
                            "NodeType": "Master",
                            "CreateTime": "2020-09-22T00:00:00+00:00",
                            "ModifyTime": "2020-09-22T00:00:00+00:00",
                            "Status": "Success",
                            "GroupId": "xxx",
                            "NetworkId": "xxx",
                            "Services": [
                                {
                                    "ServiceName": "master",
                                    "CreateTime": "2020-09-22T00:00:00+00:00",
                                    "ModifyTime": "2020-09-22T00:00:00+00:00",
                                    "Status": "Running",
                                    "KeepAlive": false,
                                    "ConfigChanged": false
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "TotalCount": 30,
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

