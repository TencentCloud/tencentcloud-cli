**Example 1: 获取Vpc列表**

获取Vpc列表

Input: 

```
tccli cloudhsm DescribeVpc --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpcList": [
            {
                "VpcName": "xxxx",
                "VpcId": "xxxxx",
                "CreatedTime": "2019-11-12 00:00:00",
                "IsDefault": false
            }
        ],
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

