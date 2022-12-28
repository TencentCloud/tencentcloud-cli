**Example 1: 查询解析记录分组列表**

 

Input: 

```
tccli dnspod DescribeRecordGroupList --cli-unfold-argument  \
    --Domain recordgroup.com \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "0076ce66-aff3-4d2b-bd6e-92bf053ae150",
        "GroupList": [
            {
                "GroupId": 0,
                "GroupName": "默认分组",
                "GroupType": "system"
            },
            {
                "GroupId": 144,
                "GroupName": "分组啊",
                "GroupType": "user"
            }
        ]
    }
}
```

