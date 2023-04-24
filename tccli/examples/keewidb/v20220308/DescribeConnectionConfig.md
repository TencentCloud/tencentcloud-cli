**Example 1: 示例1**

查询实例带宽和连接数

Input: 

```
tccli keewidb DescribeConnectionConfig --cli-unfold-argument  \
    --InstanceId kee-6ubh****
```

Output: 
```
{
    "Response": {
        "InNetLimit": 24,
        "OutNetLimit": 24,
        "ClientLimit": 10000,
        "RequestId": "e615387b-bf2b-40ac-ad3d-3b876232f547"
    }
}
```

