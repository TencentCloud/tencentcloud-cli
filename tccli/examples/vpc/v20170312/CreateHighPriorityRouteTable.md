**Example 1: 创建高优路由表**

创建高优路由表

Input: 

```
tccli vpc CreateHighPriorityRouteTable --cli-unfold-argument  \
    --VpcId vpc-mcqaoy0f \
    --Name ivan_hprtb
```

Output: 
```
{
    "Response": {
        "HighPriorityRouteTable": {
            "CreatedTime": "0000-00-00 00:00:00",
            "HighPriorityRouteSet": [],
            "HighPriorityRouteTableId": "hprtb-f9qln342",
            "Name": "ivan_hprtb",
            "VpcId": "vpc-mcqaoy0f"
        },
        "RequestId": "74e75009-1752-4127-8475-dfd12dd58a56"
    }
}
```

