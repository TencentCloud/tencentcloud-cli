**Example 1: 查询用户实例数限额**

查询用户实例数限额

Input: 

```
tccli gse DescribeInstanceLimit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Limit": 0,
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8",
        "ExtraInfos": [
            {
                "TotalInstances": 1,
                "InstanceType": "inst-sjifew"
            }
        ]
    }
}
```

