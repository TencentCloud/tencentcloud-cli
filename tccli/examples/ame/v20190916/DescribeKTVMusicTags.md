**Example 1: 获取直播互动曲库标签信息**



Input: 

```
tccli ame DescribeKTVMusicTags --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TagGroupSet": [
            {
                "EnglishGroupName": "language",
                "ChineseGroupName": "语种",
                "TagSet": [
                    {
                        "TagId": "12",
                        "TagName": "国语"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

