**Example 1: 查看种子列表**

查看种子列表

Input: 

```
tccli ctem DescribeSeeds --cli-unfold-argument  \
    --CustomerId 100136
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Category": "ip",
                "CreateAt": "2024-06-07 14:28:37",
                "CustomerId": 100136,
                "Id": 58,
                "Md5": "",
                "Source": "人工",
                "Value": "1.1.1.1"
            }
        ],
        "RequestId": "8a9e544c-6611-4364-ab0e-bea0f3d69928",
        "Total": 1
    }
}
```

