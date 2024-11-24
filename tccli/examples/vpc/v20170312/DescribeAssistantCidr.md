**Example 1: 查询辅助CIDR列表**

查询辅助CIDR列表

Input: 

```
tccli vpc DescribeAssistantCidr --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssistantCidrSet": [
            {
                "VpcId": "vpc-6v2ht8q5",
                "CidrBlock": "10.10.0.0/24",
                "AssistantType": 0,
                "SubnetSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "c65ffbe5-512a-44fd-9611-99d12f4e565d"
    }
}
```

