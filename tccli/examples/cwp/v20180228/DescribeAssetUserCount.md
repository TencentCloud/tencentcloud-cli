**Example 1: 获取所有账号数量**



Input: 

```
tccli cwp DescribeAssetUserCount --cli-unfold-argument  \
    --Name staff
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "Key": "staff",
                "Value": 10,
                "Desc": "none",
                "NewCount": 20
            }
        ],
        "RequestId": "24c9be55-c743-4a75-a5c7-2a2912341234"
    }
}
```

