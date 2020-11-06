**Example 1: 查询镜像配额**

用户需要知道自己账户一共可以持有多少镜像。

Input: 

```
tccli cvm DescribeImageQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be",
        "ImageNumQuota": 20
    }
}
```

