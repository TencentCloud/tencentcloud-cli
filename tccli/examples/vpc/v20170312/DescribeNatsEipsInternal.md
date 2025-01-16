**Example 1: 分页获取nat实例绑定的IP信息**

分页获取nat实例绑定的IP信息

Input: 

```
tccli vpc DescribeNatsEipsInternal --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EipSet": [
            "106.55.195.146",
            "106.55.193.2"
        ],
        "RequestId": "f2de8e64-c50c-46d8-af06-1c328da7201c",
        "TotalCount": 37
    }
}
```

