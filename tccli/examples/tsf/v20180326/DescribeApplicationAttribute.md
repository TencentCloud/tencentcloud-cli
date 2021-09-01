**Example 1: 获取应用列表-其它字段【前端并发调用】**



Input: 

```
tccli tsf DescribeApplicationAttribute --cli-unfold-argument  \
    --ApplicationId application-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "e852beb1-edb2-4e69-8c64-003f9aafd6ea",
        "Result": {
            "GroupCount": 1,
            "InstanceCount": 1,
            "RunInstanceCount": 1
        }
    }
}
```

