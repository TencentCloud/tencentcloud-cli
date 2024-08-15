**Example 1: 图片附件示例**



Input: 

```
tccli tandon CreateInternalTicket --cli-unfold-argument  \
    --ServiceChannel 30 \
    --InternalFeedbackUser longerwu \
    --Question 测试<br/>[img src=https://ticket-10039692.cos.ap-shanghai.myqcloud.com/1803240383_1575373437314_png]测试<br/>[attach src=https://ticket-10039692.cos.ap-shanghai.myqcloud.com/1803240383_1572321187787_test.txt] \
    --Title 自研上云测试工单 \
    --Creator raulyang
```

Output: 
```
{
    "Response": {
        "Data": {
            "TicketId": 3927491,
            "Url": "http://andon.cloud.tencent.com/ticket/nologin/redirect?id=3927491&sign=15c2c21db665ccc858e5ece2f63e1ca0"
        },
        "RequestId": "546"
    }
}
```

**Example 2: 示例**



Input: 

```
tccli tandon CreateInternalTicket --cli-unfold-argument  \
    --ServiceChannel 36 \
    --Question 问题描述 \
    --Creator raulyang
```

Output: 
```
{
    "Response": {
        "Data": {
            "TicketId": 3927491,
            "Url": "http://andon.cloud.tencent.com/ticket/nologin/redirect?id=3927491&sign=15c2c21db665ccc858e5ece2f63e1ca0"
        },
        "RequestId": "546"
    }
}
```

