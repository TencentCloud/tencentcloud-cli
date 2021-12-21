**Example 1: 嵌套查询**

通过查询的嵌套，实现知识图谱中实体N度跳转查询。

Input: 

```
tccli nlp DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "property": ["所属洲"], "subject": {"property": ["所属国家"], "subject": {"property": ["首都"], "subject": {"name": "中国"}}}}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "",
                "Name": "亚洲",
                "Popular": 0,
                "Order": 0
            }
        ],
        "RequestId": "0e113f49-853d-4ab1-af86-f504a47c68a1"
    }
}
```

**Example 2: 排序查询**

对查询结果进行排序。

Input: 

```
tccli nlp DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "order": {"direction": "decr", "property": "上映时间"}, "property": ["电影"], "subject": {"name": "梅兰芳"}, "type": ["视频类_影视明星"]}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "71d0209c-1c8f-4b3d-9c9d-edf52658345f",
                "Name": "贵妃醉酒",
                "Popular": 658,
                "Order": 0
            },
            {
                "Id": "095886bc-4bb9-4041-b8b5-7aa9aa1f1740",
                "Name": "西施",
                "Popular": 487,
                "Order": 0
            },
            {
                "Id": "507e890e-9d8d-4811-8824-b4b6c01afca1",
                "Name": "生死恨",
                "Popular": 381,
                "Order": 0
            },
            {
                "Id": "882e0876-a157-4cab-b7a9-92db3ff8d6d9",
                "Name": "梅兰芳的世界",
                "Popular": 200,
                "Order": 0
            },
            {
                "Id": "6f6aba07-c3d2-44e5-be6b-5bd7b38b275a",
                "Name": "黛玉葬花",
                "Popular": 329,
                "Order": 0
            },
            {
                "Id": "d0788847-9143-469b-a579-2c87fecea964",
                "Name": "游园惊梦",
                "Popular": 518,
                "Order": 0
            },
            {
                "Id": "c43fd30d-8407-48ec-bc0a-17b772f4f1e5",
                "Name": "洛神",
                "Popular": 445,
                "Order": 0
            },
            {
                "Id": "e9d4bf5f-0585-4b6f-9ee8-e52401f08bcc",
                "Name": "红线盗盒",
                "Popular": 553,
                "Order": 0
            },
            {
                "Id": "27da5e26-c32b-4fb0-9cb0-4cbc61c6ff38",
                "Name": "谢尔盖.爱森斯坦",
                "Popular": 131,
                "Order": 0
            },
            {
                "Id": "85f04bb3-109b-4473-b34f-b34238673e15",
                "Name": "木兰",
                "Popular": 345,
                "Order": 0
            },
            {
                "Id": "2f97f741-f160-42ef-8042-9b8cc76f173b",
                "Name": "天女散花",
                "Popular": 323,
                "Order": 0
            },
            {
                "Id": "f6ff86c6-1636-4df2-9c12-ffce53125eb9",
                "Name": "春香闹学",
                "Popular": 240,
                "Order": 0
            }
        ],
        "RequestId": "0e113f49-853d-4ab1-af86-f504a47c68a1"
    }
}
```

**Example 3: 简单PO查询**

简单PO查询表示已知宾语和谓语，查询主语，每一个PO查询都是一个可独立执行的查询。常用于推荐、搜索等业务场景。

Input: 

```
tccli nlp DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "type": ["人物类_人物"], "condition": {"and": [{"property": ["代表作品"], "equal": "文心雕龙"}]}}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "bed741ab-26c0-4d9b-80b1-75a304b2390e",
                "Name": "刘勰",
                "Popular": 719,
                "Order": 0
            },
            {
                "Id": "30947aa5-84da-4477-b64e-65780f9759b3",
                "Name": "戚德良",
                "Popular": 144,
                "Order": 0
            },
            {
                "Id": "52b3c62b-499a-4e83-aa71-8d5b9a15f6fa",
                "Name": "刘邦景",
                "Popular": 125,
                "Order": 0
            }
        ],
        "RequestId": "0e113f49-853d-4ab1-af86-f504a47c68a1"
    }
}
```

**Example 4: 简单SP查询**

简单SP查询表示已知主语和谓语查询宾语，每一个SP查询都是一个可独立执行的查询，TQL支持SP查询的嵌套查询，即主语可以是一个嵌套的子查询。

Input: 

```
tccli nlp DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "property": ["妻子"], "subject": {"name": "诸葛亮"}}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "7d88c892-c50a-42e8-b81d-c393a7b0da88",
                "Name": "黄月英",
                "Popular": 644,
                "Order": 1000
            }
        ],
        "RequestId": "0e113f49-853d-4ab1-af86-f504a47c68a1"
    }
}
```

**Example 5: 集合操作**

对多个子查询的查询结果求交或求并操作。

Input: 

```
tccli nlp DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "union": [{"property": ["代表作品"], "subject": {"name": "李白"}}, {"property": ["代表作品"], "subject": {"name": "杜甫"}}]}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "b259e95d-e399-4c66-8839-8a9a011e9ad1",
                "Name": "蜀道难",
                "Popular": 744,
                "Order": 0
            },
            {
                "Id": "dd10f9bc-1042-48cd-98a6-3b4399d63ba2",
                "Name": "茅屋为秋风所破歌",
                "Popular": 734,
                "Order": 0
            },
            {
                "Id": "454060c3-5f59-4906-8d19-9b6fac76019d",
                "Name": "梦游天姥吟留别",
                "Popular": 703,
                "Order": 0
            },
            {
                "Id": "7c9bbff1-f9f6-4ffb-bb08-da9a8987880c",
                "Name": "望岳",
                "Popular": 687,
                "Order": 0
            },
            {
                "Id": "915d354a-eb8d-481f-b55a-e0c11a38979e",
                "Name": "登高",
                "Popular": 667,
                "Order": 0
            },
            {
                "Id": "6742c919-a7b7-4278-b6e3-8e5a093b41e7",
                "Name": "春望",
                "Popular": 652,
                "Order": 0
            },
            {
                "Id": "5b8377b8-a478-4f14-8677-aa8d63318c5d",
                "Name": "静夜思",
                "Popular": 624,
                "Order": 0
            },
            {
                "Id": "b1c38da4-f778-432c-82bc-fc919d56e8e9",
                "Name": "三别",
                "Popular": 608,
                "Order": 0
            },
            {
                "Id": "cc18263a-5aeb-420e-ad3b-0bf202bea178",
                "Name": "三吏",
                "Popular": 554,
                "Order": 0
            }
        ],
        "RequestId": "0e113f49-853d-4ab1-af86-f504a47c68a1"
    }
}
```

