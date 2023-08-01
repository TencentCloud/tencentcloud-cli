**Example 1: 罗列文件系统**

列出所有的文件系统

Input: 

```
tccli goosefs DescribeFileSystems --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "FSAttributeList": [
            {
                "FileSystemId": "x_c60_r3c4fa1f",
                "Name": "MyTestFS",
                "Status": "alive",
                "Type": "goosefsx",
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
                "GooseFSxAttribute": {
                    "Model": "C60",
                    "Capacity": 4608,
                    "MappedBucketList": [
                        {
                            "BucketName": "mybucket-12500000",
                            "FileSystemPath": "/"
                        }
                    ],
                    "ClientManagerNodeList": [
                        {
                            "NodeInstanceId": "ins-a1b2c3",
                            "NodeIp": "10.0.1.1",
                            "InitialPassword": "a1b2c3d4"
                        },
                        {
                            "NodeInstanceId": "ins-d4f5g6",
                            "NodeIp": "10.0.1.2",
                            "InitialPassword": "a1b2c3d4"
                        },
                        {
                            "NodeInstanceId": "ins-h7i8j9",
                            "NodeIp": "10.0.1.3",
                            "InitialPassword": "a1b2c3d4"
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

