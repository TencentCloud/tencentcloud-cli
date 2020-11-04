**Example 1: 查询终端用户注册状态**



Input: 

```
tccli iotvideo DescribeRegistrationStatus --cli-unfold-argument  \
    --CunionIds test000 test001
```

Output: 
```
{
    "Response": {
        "RequestId": "b9b35fd0-52a9-415e-809d-d49f9fa1fafa",
        "Data": [
            {
                "CunionId": "test000",
                "IsRegisted": false
            },
            {
                "CunionId": "test001",
                "IsRegisted": true
            }
        ]
    }
}
```

