**Example 1: 查询指定云服务器是否支持巨帧**

查询指定云服务器是否支持巨帧。

Input: 

```
tccli vpc DescribeInstanceJumbo --cli-unfold-argument  \
    --InstanceIds ins-70w096mg ins-71b1qyss
```

Output: 
```
{
    "Response": {
        "InstanceJumboSet": [
            {
                "InstanceId": "ins-70w096mg",
                "JumboState": false
            }
        ],
        "RequestId": "7fc40006-3629-44de-a520-74ffd2cf1882"
    }
}
```

