**Example 1: 获取自定义脚本任务详细信息**



Input: 

```
tccli bm DescribeUserCmdTaskInfo --cli-unfold-argument  \
    --TaskId cmdtask-mi5k1oct \
    --Offset 0 \
    --Limit 20 \
    --OrderField RunBeginTime \
    --Order 1 \
    --SearchKey m
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "UserCmdTaskInfoSet": [
            {
                "AutoId": 4,
                "TaskId": "cmdtask-abc1",
                "RunBeginTime": "2018-09-20 17:42:21",
                "RunEndTime": "",
                "Status": -1,
                "InstanceName": "xxx1",
                "InstanceId": "cpm-aaa",
                "VpcName": "asdas",
                "VpcId": "vpc-123",
                "VpcCidrBlock": "10.88.0.0/16",
                "SubnetName": "asdadads",
                "SubnetId": "subnet-123",
                "SubnetCidrBlock": "10.88.0.0/24",
                "LanIp": "10.88.0.3",
                "CmdContent": "IyEvYmluL2Jhc2gKZm9yIGkgaW4gezEuLjEwMH0KZG8KICAgIGVjaG8gJGkKCXNsZWVwIDEwCmRvbmUK",
                "CmdParam": "",
                "CmdResult": "",
                "AppId": 123,
                "LastShellExit": -1
            },
            {
                "AutoId": 5,
                "TaskId": "cmdtask-abc2",
                "RunBeginTime": "2018-09-20 17:42:21",
                "RunEndTime": "",
                "Status": -1,
                "InstanceName": "xxxxx",
                "InstanceId": "cpm-bbb",
                "VpcName": "dsffdssfd",
                "VpcId": "vpc-234",
                "VpcCidrBlock": "10.88.0.0/16",
                "SubnetName": "fdsfdsfds",
                "SubnetId": "subnet-234",
                "SubnetCidrBlock": "10.88.255.0/24",
                "LanIp": "10.88.255.2",
                "CmdContent": "IyEvYmluL2Jhc2gKZm9yIGkgaW4gezEuLjEwMH0KZG8KICAgIGVjaG8gJGkKCXNsZWVwIDEwCmRvbmUK",
                "CmdParam": "",
                "CmdResult": "",
                "AppId": 123,
                "LastShellExit": -1
            }
        ],
        "RequestId": "da45b829-bbe4-4e49-b85e-e9cd0aeeb139"
    }
}
```

