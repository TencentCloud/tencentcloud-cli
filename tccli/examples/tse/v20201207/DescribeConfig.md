**Example 1: 查看配置**

查看配置

Input: 

```
tccli tse DescribeConfig --cli-unfold-argument  \
    --InstanceId ins-389a8c12 \
    --Type consul \
    --Key name
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "Key": "name",
        "Value": "tom",
        "IsDir": false,
        "List": []
    }
}
```

