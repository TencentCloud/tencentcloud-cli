**Example 1: 获取成功示例**

获取成功

Input: 

```
tccli cms DescribeLevelTag --cli-unfold-argument  \
    --ParentTag  \
    --Type Text
```

Output: 
```
{
    "Response": {
        "LevelTagList": [
            {
                "Code": "100",
                "Name": "Normal",
                "Cname": "正常",
                "Scene": "",
                "Priority": 0,
                "FontColor": "#008000",
                "BackGroundColor": "#008000",
                "TagType": "Other"
            },
            {
                "Code": "20001",
                "Name": "Polity",
                "Cname": "政治",
                "Scene": "",
                "Priority": 999,
                "FontColor": "#000000",
                "BackGroundColor": "#E54545",
                "TagType": "Other"
            },
            {
                "Code": "20105",
                "Name": "Ad",
                "Cname": "广告",
                "Scene": "",
                "Priority": 750,
                "FontColor": "",
                "BackGroundColor": "#149CFF",
                "TagType": "Other"
            },
            {
                "Code": "20007",
                "Name": "Abuse",
                "Cname": "谩骂",
                "Scene": "",
                "Priority": 800,
                "FontColor": "",
                "BackGroundColor": "#9741D9",
                "TagType": "Other"
            },
            {
                "Code": "20006",
                "Name": "Illegal",
                "Cname": "违法",
                "Scene": "",
                "Priority": 900,
                "FontColor": "",
                "BackGroundColor": "#4B70F5",
                "TagType": "Other"
            },
            {
                "Code": "25001",
                "Name": "Spam",
                "Cname": "灌水",
                "Scene": "",
                "Priority": 700,
                "FontColor": "",
                "BackGroundColor": "#1FC0CC",
                "TagType": "Other"
            },
            {
                "Code": "24001",
                "Name": "Terror",
                "Cname": "暴恐",
                "Scene": "",
                "Priority": 950,
                "FontColor": "",
                "BackGroundColor": "#FF7200",
                "TagType": "Other"
            },
            {
                "Code": "20002",
                "Name": "Porn",
                "Cname": "色情",
                "Scene": "",
                "Priority": 970,
                "FontColor": "",
                "BackGroundColor": "#FFBB00",
                "TagType": "Other"
            }
        ],
        "RequestId": "afb5ce6e-b68b-4da2-be4e-cf783ae4a91e"
    }
}
```

**Example 2: 分级标签查询和返回**

分级标签

Input: 

```
tccli cms DescribeLevelTag --cli-unfold-argument  \
    --Type abc \
    --ParentTag abc
```

Output: 
```
{
    "Response": {
        "LevelTagList": [
            {
                "Code": "abc",
                "Name": "abc",
                "Cname": "abc",
                "Scene": "abc",
                "Priority": 0,
                "FontColor": "abc",
                "BackGroundColor": "abc",
                "TagType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

