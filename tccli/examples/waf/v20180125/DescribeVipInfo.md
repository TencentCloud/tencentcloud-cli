**Example 1: 查询vip**

查询实例的vip信息

Input: 

```
tccli waf DescribeVipInfo --cli-unfold-argument  \
    --InstanceIds abc
```

Output: 
```
{
    "Response": {
        "VipInfo": [
            {
                "Vip": "abc",
                "InstanceId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

