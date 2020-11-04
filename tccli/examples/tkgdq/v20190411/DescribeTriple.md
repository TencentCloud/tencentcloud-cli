**Example 1: 嵌套查询**

通过查询的嵌套，实现知识图谱中实体N度跳转查询。

Input: 

```
tccli tkgdq DescribeTriple --cli-unfold-argument  \
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
        "RequestId": "5931f8ff-204d-4001-9952-ee6618eeabe1"
    }
}
```

**Example 2: 排序查询**

对查询结果进行排序。

Input: 

```
tccli tkgdq DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "order": {"direction": "decr", "property": "上映时间"}, "property": ["电影"], "subject": {"name": "梅兰芳"}, "type": ["视频类_影视明星"]}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "6385682411239590016",
                "Name": "贵妃醉酒",
                "Popular": 658,
                "Order": 0
            },
            {
                "Id": "97672352249307577",
                "Name": "黛玉葬花",
                "Popular": 329,
                "Order": 0
            },
            {
                "Id": "3872879001691542503",
                "Name": "游园惊梦",
                "Popular": 513,
                "Order": 0
            },
            {
                "Id": "6039452215267501920",
                "Name": "洛神",
                "Popular": 445,
                "Order": 0
            },
            {
                "Id": "874155246214489324",
                "Name": "生死恨",
                "Popular": 619,
                "Order": 0
            },
            {
                "Id": "1697700977748569723",
                "Name": "红线盗盒",
                "Popular": 553,
                "Order": 0
            },
            {
                "Id": "1764444282223233977",
                "Name": "谢尔盖.爱森斯坦",
                "Popular": 131,
                "Order": 0
            },
            {
                "Id": "18020014071881122456",
                "Name": "木兰从军",
                "Popular": 323,
                "Order": 0
            },
            {
                "Id": "3084383882260523320",
                "Name": "天女散花",
                "Popular": 323,
                "Order": 0
            },
            {
                "Id": "4548611187049221674",
                "Name": "虞姬舞剑",
                "Popular": 200,
                "Order": 0
            },
            {
                "Id": "4758047787955938561",
                "Name": "上元夫人",
                "Popular": 200,
                "Order": 0
            },
            {
                "Id": "2113278850746938975",
                "Name": "春香闹学",
                "Popular": 240,
                "Order": 0
            }
        ],
        "RequestId": "ba593da1-eccd-42b5-acd9-e95ef6d37804"
    }
}
```

**Example 3: 简单PO查询**

简单PO查询表示已知宾语和谓语，查询主语，每一个PO查询都是一个可独立执行的查询。常用于推荐、搜索等业务场景。

Input: 

```
tccli tkgdq DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "type": ["人物类_人物"], "condition": {"and": [{"property": ["代表作品"], "equal": "文心雕龙"}]}}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "2043040489539444929",
                "Name": "刘勰",
                "Popular": 719,
                "Order": 0
            },
            {
                "Id": "9413806637648188367",
                "Name": "丹徒人",
                "Popular": 418,
                "Order": 0
            },
            {
                "Id": "3189922825914104695",
                "Name": "戚德良",
                "Popular": 144,
                "Order": 0
            },
            {
                "Id": "1277357571304718209",
                "Name": "刘邦景",
                "Popular": 125,
                "Order": 0
            }
        ],
        "RequestId": "e39d2f69-1c74-41e4-bd5c-994899fdf781"
    }
}
```

**Example 4: 简单SP查询**

简单SP查询表示已知主语和谓语查询宾语，每一个SP查询都是一个可独立执行的查询，TQL支持SP查询的嵌套查询，即主语可以是一个嵌套的子查询。

Input: 

```
tccli tkgdq DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "property": ["妻子"], "subject": {"name": "诸葛亮"}}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "1427806415100612517",
                "Name": "黄月英",
                "Popular": 644,
                "Order": 1000
            }
        ],
        "RequestId": "a7a92303-bb64-4904-b957-4c344de41725"
    }
}
```

**Example 5: 集合操作**

对多个子查询的查询结果求交或求并操作。

Input: 

```
tccli tkgdq DescribeTriple --cli-unfold-argument  \
    --TripleCondition '{"operation": "query", "union": [{"property": ["代表作品"], "subject": {"name": "李白"}}, {"property": ["代表作品"], "subject": {"name": "杜甫"}}]}'
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Id": "2040123437182277220",
                "Name": "蜀道难",
                "Popular": 744,
                "Order": 0
            },
            {
                "Id": "487527294230960076",
                "Name": "茅屋为秋风所破歌",
                "Popular": 734,
                "Order": 0
            },
            {
                "Id": "1455284150188265913",
                "Name": "梦游天姥吟留别",
                "Popular": 703,
                "Order": 0
            },
            {
                "Id": "930802421448490072",
                "Name": "望岳",
                "Popular": 687,
                "Order": 0
            },
            {
                "Id": "591095700822340523",
                "Name": "将进酒",
                "Popular": 676,
                "Order": 0
            },
            {
                "Id": "3559237438616619919",
                "Name": "登高",
                "Popular": 667,
                "Order": 0
            },
            {
                "Id": "1331369627105961920",
                "Name": "春望",
                "Popular": 652,
                "Order": 0
            },
            {
                "Id": "2431867642048154231",
                "Name": "静夜思",
                "Popular": 624,
                "Order": 0
            },
            {
                "Id": "11373670987754702313",
                "Name": "三别",
                "Popular": 608,
                "Order": 0
            },
            {
                "Id": "1731436860982500306",
                "Name": "三吏",
                "Popular": 554,
                "Order": 0
            }
        ],
        "RequestId": "91642c1b-017c-4ece-b4f4-e22e694f16a5"
    }
}
```

