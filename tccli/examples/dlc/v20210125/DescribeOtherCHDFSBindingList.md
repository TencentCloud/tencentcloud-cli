**Example 1: 示例**

示例

Input: 

```
tccli dlc DescribeOtherCHDFSBindingList --cli-unfold-argument  \
    --BucketId abc
```

Output: 
```
{
    "Response": {
        "OtherCHDFSBindingList": [
            {
                "ProductName": "abc",
                "SuperUser": [
                    "abc"
                ],
                "VpcInfo": [
                    {
                        "VpcId": "abc",
                        "VpcName": "abc",
                        "VpcCidrBlock": [
                            {
                                "CidrId": "abc",
                                "CidrAddr": "abc"
                            }
                        ]
                    }
                ],
                "IsBind": true
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

