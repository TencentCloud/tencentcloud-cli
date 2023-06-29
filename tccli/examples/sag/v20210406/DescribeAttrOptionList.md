**Example 1: 获取属性选项列表**



Input: 

```
tccli sag DescribeAttrOptionList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AttrList": [
            {
                "Id": 1,
                "Name": "任意属性"
            }
        ],
        "CondList": [
            {
                "Id": 1,
                "Name": "任意条件"
            }
        ],
        "RequestId": "xxx"
    }
}
```

