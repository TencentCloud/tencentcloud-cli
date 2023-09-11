**Example 1: 查询地址模板列表**



Input: 

```
tccli cfw DescribeAddressTemplateList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --By abc \
    --Order abc \
    --SearchValue abc
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Data": [
            {
                "Uuid": "abc",
                "Name": "abc",
                "Detail": "abc",
                "IpString": "abc",
                "InsertTime": "abc",
                "UpdateTime": "abc",
                "Type": 0,
                "RulesNum": 0
            }
        ],
        "NameList": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

