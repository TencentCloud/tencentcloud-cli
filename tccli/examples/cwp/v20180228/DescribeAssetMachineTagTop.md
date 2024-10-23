**Example 1: 获取主机标签Top5**



Input: 

```
tccli cwp DescribeAssetMachineTagTop --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "24c9be55-c743-4a75-a5c7-2a2912341234",
        "Tags": [
            {
                "Value": 10,
                "Desc": "abc",
                "Key": "total",
                "NewCount": 0
            }
        ]
    }
}
```

