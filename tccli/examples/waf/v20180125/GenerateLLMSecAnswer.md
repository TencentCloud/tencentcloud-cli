**Example 1: 流式响应测试用例**



Input: 

```
tccli waf GenerateLLMSecAnswer --cli-unfold-argument  \
    --Message.Role user \
    --Message.Content 你能干些什么 \
    --Message.ContentType 1 \
    --MsgID test-001
```

Output: 
```
流式响应输出格式：
data: {"index":1,"success":true,"data":"您好"}

data: {"index":2,"success":true,"data":"！"}

data: {"index":3,"success":true,"data":"我"}

data: {"index":4,"success":true,"data":"是一款"}

data: {"index":5,"success":true,"data":"人工智能"}

data: {"index":6,"success":true,"data":"助手"}

data: {"index":7,"success":true,"data":"，"}

data: {"index":8,"success":true,"data":"名为"}

data: {"index":9,"success":true,"data":"腾讯"}

data: {"index":10,"success":true,"data":"元宝"}

data: {"index":11,"success":true,"data":"。"}

data: {"index":12,"success":true,"data":"我可以"}

data: {"index":13,"success":true,"data":"回答"}

data: {"index":14,"success":true,"data":"您"}

data: {"index":15,"success":true,"data":"的问题"}

data: {"index":16,"success":true,"data":"、"}

data: {"index":17,"success":true,"data":"提供"}

data: {"index":18,"success":true,"data":"信息"}

data: {"index":19,"success":true,"data":"和建议"}

data: {"index":20,"success":true,"data":"，"}

data: {"index":21,"success":true,"data":"甚至"}

data: {"index":22,"success":true,"data":"进行"}

data: {"index":23,"success":true,"data":"简单的"}

data: {"index":24,"success":true,"data":"对话"}

data: {"index":25,"success":true,"data":"。"}

data: {"index":26,"success":true,"data":"我的"}

data: {"index":27,"success":true,"data":"目的是"}

data: {"index":28,"success":true,"data":"为您提供"}

data: {"index":29,"success":true,"data":"帮助"}

data: {"index":30,"success":true,"data":"和支持"}

data: {"index":31,"success":true,"data":"。"}

data: {"index":32,"success":true,"data":"有什么"}

data: {"index":33,"success":true,"data":"可以"}

data: {"index":34,"success":true,"data":"帮"}

data: {"index":35,"success":true,"data":"您的"}

data: {"index":36,"success":true,"data":"吗"}

data: {"index":37,"success":true,"data":"？"}

data: {"index":38,"success":true,"end":true}
```

