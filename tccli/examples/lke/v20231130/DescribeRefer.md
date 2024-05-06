**Example 1: 查询参考来源详情**

查询参考来源详情

Input: 

```
tccli lke DescribeRefer --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --ReferBizIds 1694302461379890134
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Answer": "",
                "Confidence": 0.9336649,
                "DocName": "《深海余烬》.txt",
                "DocType": 2,
                "Highlights": [],
                "Mark": 1,
                "OrgData": "《深海余烬》: \r\n    没有人会想到异象001有朝一日会出问题，就像没有人考虑过无垠海会不会在某一天干涸。\r\n    然而现在看来，这「永恒」的太阳也并不是真的永恒。\r\n    先是日出推迟了十五分钟，随后是符文圆环上那个肉眼几乎无法分辨的缺口……这些令人不安的信息都在说明一件事：异象001的寿命竟然是有限的！\r\n    邓肯站在橱窗旁边，默默地看着明亮的天光照亮街道，脑海中的纷繁思绪却如风暴一般翻涌着。\r\n    注意到太阳异变的绝不只有自己，世界上的聪明人很多，普通人或许不会关注头顶上的变化，但各个城邦当局以及教会肯定有人时刻盯着这个世界上最大的异象，现在，应该就已经有人注意到了太阳的变化……他们会如何想？他们会如何应对？是否有人知道发生了什么？\r\n",
                "PageContent": "《深海余烬》: \r\n    没有人会想到异象001有朝一日会出问题，就像没有人考虑过无垠海会不会在某一天干涸。\r\n    然而现在看来，这「永恒」的太阳也并不是真的永恒。\r\n    先是日出推迟了十五分钟，随后是符文圆环上那个肉眼几乎无法分辨的缺口……这些令人不安的信息都在说明一件事：异象001的寿命竟然是有限的！\r\n    邓肯站在橱窗旁边，默默地看着明亮的天光照亮街道，脑海中的纷繁思绪却如风暴一般翻涌着。\r\n    注意到太阳异变的绝不只有自己，世界上的聪明人很多，普通人或许不会关注头顶上的变化，但各个城邦当局以及教会肯定有人时刻盯着这个世界上最大的异象，现在，应该就已经有人注意到了太阳的变化……他们会如何想？他们会如何应对？是否有人知道发生了什么？\r\n",
                "Question": "",
                "ReferBizId": "1694302461379890134"
            }
        ],
        "RequestId": "73e3226c-b180-4b21-923b-2bfcc47b96bc"
    }
}
```
