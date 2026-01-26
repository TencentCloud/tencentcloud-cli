**Example 1: 查询文件系统的客户端集群**



Input: 

```
tccli goosefs DescribeCustomerCluster --cli-unfold-argument  \
    --FileSystemId x-c60-412s8jlp
```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "ClientNum": 0,
                "ClusterId": "x-c60-412s8jlp",
                "ClusterName": "test_cluster",
                "ClusterType": 0,
                "ManagerNodes": [
                    {
                        "ClusterId": "x-c60-412s8jlp",
                        "InitialPassword": "*****",
                        "NodeInstanceId": "ins-20jxbhdb",
                        "NodeIp": "10.1.16.93"
                    }
                ],
                "Status": 0,
                "SubnetId": "subnet-ekn2txsv",
                "VpcId": "vpc-q6lm145g"
            }
        ],
        "RequestId": "13448a6b-8145-4f4a-960d-3db9427b6357"
    }
}
```

