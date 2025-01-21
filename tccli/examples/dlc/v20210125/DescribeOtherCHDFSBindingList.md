**Example 1: 示例**

示例

Input: 

```
tccli dlc DescribeOtherCHDFSBindingList --cli-unfold-argument  \
    --BucketId dlcce79-*-*-*-*
```

Output: 
```
{
    "Response": {
        "OtherCHDFSBindingList": [
            {
                "ProductName": "other",
                "SuperUser": [
                    "root"
                ],
                "VpcInfo": [
                    {
                        "RuleId": 1111,
                        "AccessGroupId": "ag-234",
                        "VpcId": "vpc-123456",
                        "VpcName": "",
                        "VpcCidrBlock": [
                            {
                                "CidrId": "",
                                "CidrAddr": "10.*.*.*/16"
                            }
                        ]
                    }
                ],
                "IsBind": false
            },
            {
                "ProductName": "other",
                "SuperUser": [
                    "root"
                ],
                "VpcInfo": [
                    {
                        "RuleId": 2222,
                        "AccessGroupId": "ag-123",
                        "VpcId": "vpc-123456",
                        "VpcName": "",
                        "VpcCidrBlock": [
                            {
                                "CidrId": "",
                                "CidrAddr": "172.*.*.*/16"
                            }
                        ]
                    }
                ],
                "IsBind": true
            }
        ],
        "RequestId": "3f110545-d05a-4c7c-a851-94c11cf9d4c2",
        "Total": 2
    }
}
```

