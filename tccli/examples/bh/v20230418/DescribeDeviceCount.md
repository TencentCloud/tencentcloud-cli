**Example 1: 查询堡垒机服务已经导入的主机数**

查询堡垒机服务已经导入的主机数

Input: 

```
tccli bh DescribeDeviceCount --cli-unfold-argument  \
    --ResourceId bh-saas-1jku8g
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

**Example 2: 查询导入的主机总数**

查询全部已导入的主机数

Input: 

```
tccli bh DescribeDeviceCount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

