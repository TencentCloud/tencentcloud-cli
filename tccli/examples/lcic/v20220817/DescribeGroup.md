**Example 1: 获取群组详情**

获取群组详情

Input: 

```
tccli lcic DescribeGroup --cli-unfold-argument  \
    --GroupId abcdfdfg \
    --SdkAppId 12345678
```

Output: 
```
{
    "Response": {
        "GroupId": "9012",
        "GroupName": "test",
        "TeacherId": "jklP90Mp",
        "GroupType": 1,
        "SubGroupIds": [
            "12290"
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

