**Example 1: 索引获取token**

索引获取token登录space维度的kibana

Input: 

```
tccli es DescribeSpaceKibanaTools --cli-unfold-argument  \
    --SpaceId abc
```

Output: 
```
{
    "Response": {
        "KibanaToken": "abc",
        "ExpireTime": 0,
        "RequestId": "abc"
    }
}
```

**Example 2: kibana内嵌登录token获取**

用于登录space维度的内嵌的kibana

Input: 

```
tccli es DescribeSpaceKibanaTools --cli-unfold-argument  \
    --SpaceId abc
```

Output: 
```
{
    "Response": {
        "KibanaToken": "abc",
        "ExpireTime": 0,
        "RequestId": "abc"
    }
}
```

