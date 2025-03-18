**Example 1: 罗列文件系统**

列出所有的文件系统

Input: 

```
tccli goosefs DescribeFileSystems --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "FSAttributeList": [
            {
                "ChargeAttribute": {
                    "PayMode": "postPay"
                },
                "CreateTime": "2025-03-06T20:25:17+08:00",
                "Description": "性能",
                "FileSystemId": "x-c50-6zgr1g24",
                "GooseFSxAttribute": {
                    "Capacity": 9216,
                    "ClientManagerNodeList": [
                        {
                            "InitialPassword": "wcewcffevvrvvrvgr",
                            "NodeInstanceId": "ins-3nryi8i7",
                            "NodeIp": "10.0.0.10"
                        },
                        {
                            "InitialPassword": "wcewcffevvrvvrvgr",
                            "NodeInstanceId": "ins-h84056df",
                            "NodeIp": "10.0.0.11"
                        },
                        {
                            "InitialPassword": "wcewcffevvrvvrvgr",
                            "NodeInstanceId": "ins-0voabq4p",
                            "NodeIp": "10.0.0.12"
                        }
                    ],
                    "MappedBucketList": [],
                    "Model": "C50"
                },
                "ModifyTime": "2025-03-06T20:39:10+08:00",
                "Name": "性能",
                "Status": "ACTIVE",
                "SubnetId": "subnet-c4cdynlr",
                "Tag": [],
                "Type": "goosefsx",
                "VpcId": "vpc-lc0aecbo",
                "Zone": "ap-beijing-7"
            },
            {
                "ChargeAttribute": {
                    "PayMode": "postPay"
                },
                "CreateTime": "2025-03-05T17:12:03+08:00",
                "Description": "s6C50",
                "FileSystemId": "x-c50-q51r4u2f",
                "GooseFSxAttribute": {
                    "Capacity": 9216,
                    "ClientManagerNodeList": [
                        {
                            "InitialPassword": "wcewcffevvrvvrvgr",
                            "NodeInstanceId": "ins-1z4swav5",
                            "NodeIp": "10.0.0.1"
                        },
                        {
                            "InitialPassword": "wcewcffevvrvvrvgr",
                            "NodeInstanceId": "ins-6dzh6vd3",
                            "NodeIp": "10.0.0.11"
                        },
                        {
                            "InitialPassword": "wcewcffevvrvvrvgr",
                            "NodeInstanceId": "ins-70nmym9x",
                            "NodeIp": "10.0.0.12"
                        }
                    ],
                    "MappedBucketList": [],
                    "Model": "C50"
                },
                "ModifyTime": "2025-03-05T17:26:16+08:00",
                "Name": "s6C50",
                "Status": "ACTIVE",
                "SubnetId": "subnet-c4cdynlr",
                "Tag": [],
                "Type": "goosefsx",
                "VpcId": "vpc-lc0aecbo",
                "Zone": "ap-beijing-7"
            }
        ],
        "RequestId": "7066c1c9-5b5d-494c-8116-1c6f533ee2f6",
        "TotalCount": 2
    }
}
```

