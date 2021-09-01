**Example 1: 获取服务器实例类型列表**

获取服务器实例类型列表

Input: 

```
tccli gse DescribeInstanceTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceTypeList": [
            {
                "TypeName": "标准型S3",
                "InstanceType": "S3.LARGE8",
                "Cpu": 4,
                "Memory": 8,
                "NetworkCard": 45
            }
        ],
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

