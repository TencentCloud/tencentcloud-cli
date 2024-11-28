**Example 1: 获取Vpc列表**

获取Vpc列表

Input: 

```
tccli cloudhsm DescribeVpc --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "53f36372-7b0e-4a24-879b-1f8b877023a0",
        "TotalCount": 1,
        "VpcList": [
            {
                "CreatedTime": "2024-05-09 19:51:48",
                "IsDefault": false,
                "VpcId": "vpc-nc9yvu5p",
                "VpcName": "test_5"
            }
        ]
    }
}
```

