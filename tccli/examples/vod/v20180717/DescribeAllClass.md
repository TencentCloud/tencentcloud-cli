**Example 1: 获取视频分类层次结构**



Input: 

```
tccli vod DescribeAllClass --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ClassInfoSet": [
            {
                "ClassId": 0,
                "Level": 0,
                "ClassName": "其他",
                "ParentId": -1,
                "Name": "abc",
                "SubClassIdSet": []
            },
            {
                "ClassId": 1,
                "Level": 0,
                "ClassName": "自定义一级分类",
                "ParentId": -1,
                "Name": "1",
                "SubClassIdSet": [
                    2,
                    3
                ]
            },
            {
                "ClassId": 2,
                "Level": 2,
                "ClassName": "自定义二级分类",
                "ParentId": 1,
                "Name": "2",
                "SubClassIdSet": [
                    4,
                    5
                ]
            },
            {
                "ClassId": 3,
                "Level": 2,
                "ClassName": "自定义二级分类",
                "ParentId": 1,
                "Name": "3",
                "SubClassIdSet": []
            }
        ],
        "RequestId": "requestId"
    }
}
```

