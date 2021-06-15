**Example 1: 设置标签库**



Input: 

```
tccli wav CreateCorpTag --cli-unfold-argument  \
    --GroupName xx \
    --Sort 0 \
    --Tags.0.TagName xx \
    --Tags.0.Sort 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TagGroup": {
            "GroupId": "TAG_GROUPID1",
            "BizGroupId": 1348107208961921026,
            "GroupName": "GOURP_NAME",
            "CreateTime": 1557838797,
            "Sort": 1,
            "Tags": [
                {
                    "TagId": "TAG_ID1",
                    "BizTagId": 1348107111961921026,
                    "TagName": "NAME1",
                    "CreateTime": 1557838797,
                    "Sort": 1
                }
            ]
        }
    }
}
```

