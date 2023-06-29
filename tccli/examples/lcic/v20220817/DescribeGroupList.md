**Example 1: 获取群组列表**

获取群组列表

Input: 

```
tccli lcic DescribeGroupList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Total": 1,
        "GroupInfos": [
            {
                "GroupId": "adfgdfg",
                "GroupName": "test",
                "GroupType": 0
            }
        ]
    }
}
```

