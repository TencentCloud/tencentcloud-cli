**Example 1: 查询实例创建镜像属性**

查询实例创建镜像属性

Input: 

```
tccli lighthouse DescribeInstancesCreateBlueprintAttributes --cli-unfold-argument  \
    --InstanceIds lhins-9tnyxdje
```

Output: 
```
{
    "Response": {
        "InstanceCreateBlueprintAttributesSet": [
            {
                "InstanceId": "lhins-9tnyxdje",
                "SupportOnlineCreateBlueprint": true
            }
        ],
        "RequestId": "601be4eb-7280-44ea-8515-2b1044ff68c7"
    }
}
```

