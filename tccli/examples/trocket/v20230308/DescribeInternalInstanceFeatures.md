**Example 1: 查询实例开启的特性列表**

查询实例开启的特性列表

Input: 

```
tccli trocket DescribeInternalInstanceFeatures --cli-unfold-argument  \
    --InstanceId rmq-4k4orqgq
```

Output: 
```
{
    "Response": {
        "Features": [
            {
                "Feature": "DetailedAcl",
                "ResourceId": "rmq-4k4orqgq"
            }
        ],
        "RequestId": "d260e26f-e8a2-4582-8290-69bb743054e0"
    }
}
```

