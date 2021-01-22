**Example 1: 查看资源标签列表**

查看资源标签列表

Input: 

```
tccli chdfs DescribeResourceTags --cli-unfold-argument  \
    --FileSystemId f4mhaqkciq0
```

Output: 
```
{
    "Response": {
        "Tags": [
            {
                "Key": "key1",
                "Value": "value1"
            },
            {
                "Key": "key2",
                "Value": "value2"
            }
        ],
        "RequestId": "22e36f95-9295-4132-a75e-09a08d2e13fc"
    }
}
```

