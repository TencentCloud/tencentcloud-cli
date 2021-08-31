**Example 1: 查询基线详情**

根据基线id查询基线详情

Input: 

```
tccli cwp DescribeBaselineDetail --cli-unfold-argument  \
    --BaselineId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "BaselineDetail": {
            "Description": "基线详情描述",
            "Level": 1,
            "PackageName": "xx",
            "ParentId": 1,
            "Name": "xx"
        }
    }
}
```

