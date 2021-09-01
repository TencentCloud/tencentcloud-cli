**Example 1: 查询VPC列表**



Input: 

```
tccli bmvpc DescribeVpcs --cli-unfold-argument  \
    --VpcIds vpc-ox7p0l9u vpc-jvxdy07y
```

Output: 
```
{
    "Response": {
        "VpcSet": [
            {
                "VpcId": "vpc-ox7p0l9u",
                "VpcName": "autocreate_20180320",
                "CidrBlock": "10.104.0.0/16",
                "Zone": "1000100003",
                "State": "available",
                "CreateTime": "2018-03-20 11:40:49"
            },
            {
                "VpcId": "vpc-jvxdy07y",
                "VpcName": "test-vpc",
                "CidrBlock": "172.16.0.0/16",
                "Zone": "1000100003",
                "State": "available",
                "CreateTime": "2018-06-12 10:13:17"
            }
        ],
        "RequestId": "72899e7e-dbeb-4add-bf8f-8efe5a315f98"
    }
}
```

