**Example 1: kibana内嵌登录token获取**

用于登录space维度的内嵌的kibana

Input: 

```
tccli es DescribeSpaceKibanaTools --cli-unfold-argument  \
    --SpaceId space-eafijiaef
```

Output: 
```
{
    "Response": {
        "KibanaToken": "feijfioajefbifiejiaUFHieuf",
        "ExpireTime": 1742806292,
        "RequestId": "40f4f780-9969-42f9-8bd9-ccf0d1f2591a"
    }
}
```

