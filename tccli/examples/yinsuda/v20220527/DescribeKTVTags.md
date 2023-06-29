**Example 1: 获取标签列表**



Input: 

```
tccli yinsuda DescribeKTVTags --cli-unfold-argument  \
    --UserId 20220123abc \
    --AppName test
```

Output: 
```
{
    "Response": {
        "TagGroupInfoSet": [
            {
                "GroupId": "1",
                "TagInfoSet": [
                    {
                        "TagId": "11",
                        "Name": "嘻哈"
                    }
                ],
                "Name": "风格"
            }
        ],
        "RequestId": "58bfe77f-d477-48e8-9922-55f56d0b88fb"
    }
}
```

