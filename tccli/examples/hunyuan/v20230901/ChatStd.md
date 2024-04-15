**Example 1: 多轮对话示例**

多轮对话场景

Input: 

```
tccli hunyuan ChatStd --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Messages.0.Role user \
    --Messages.0.Content 请介绍下自己 \
    --Messages.1.Role assistant \
    --Messages.1.Content 我的名字是腾讯混元大模型，是腾讯开发的一款大型语言模型。我能够理解人类语言，擅长提供问答服务、常识推理、文本创作、数学计算和互动问答等服务。如果您需要帮助或有任何问题，请随时向我提问。 \
    --Messages.2.Role user \
    --Messages.2.Content 请给我讲个字数小于10个字的搞笑笑话 \
    --Messages.3.Role assistant \
    --Messages.3.Content 猫头鹰遇见眯眯眼，看得眼睛都眯成线。” \
    --Messages.4.Role user \
    --Messages.4.Content 不好笑，换一个吧
```

Output: 
```
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"老鼠"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":1,"TotalTokens":86}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"遇见"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":2,"TotalTokens":87}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"猫"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":3,"TotalTokens":88}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"，"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":4,"TotalTokens":89}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"逃"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":5,"TotalTokens":90}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"得"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":6,"TotalTokens":91}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"比"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":7,"TotalTokens":92}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"闪电"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":8,"TotalTokens":93}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"快"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":9,"TotalTokens":94}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"。"}}],"Created":1705635290,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":10,"TotalTokens":95}}
 {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"stop","Delta":{"Role":"assistant","Content":""}}],"Created":1705635291,"Id":"eb53a6d6-c000-4b74-aad2-a8e82540518a","Usage":{"PromptTokens":85,"CompletionTokens":10,"TotalTokens":95}}
```

**Example 2: 请求失败示例**



Input: 

```
tccli hunyuan ChatStd --cli-unfold-argument  \
    --TopP 0 \
    --Temperature 4.8 \
    --Messages.0.Role user \
    --Messages.0.Content 介绍下自己
```

Output: 
```
{
    "Response": {
        "RequestId": "655c67aad32b0f48f52b89b0",
        "Error": {
            "Code": "InvalidParameter",
            "Message": "The value of Temperature should be within the range [0.0, 2.0]: 4.800000 "
        }
    }
}
```

**Example 3: 流式请求成功示例**



Input: 

```
tccli hunyuan ChatStd --cli-unfold-argument  \
    --TopP 0 \
    --Stream True \
    --Temperature 0 \
    --Messages.0.Role user \
    --Messages.0.Content 计算1+1
```

Output: 
```
HTTP/1.1 200 OK
Cache-Control: no-cache
Connection: keep-alive
Content-Type: text/event-stream
Date: Tue, 21 Nov 2023 06:56:00 GMT
Transfer-Encoding: chunked
X-TC-RequestId: 61a8459b-27c8-4868-af8f-f374db0245f8

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"1"}}],"Created":1700549760,"Id":"148b89ef-14e1-489f-8e70-b767e5b27d56","Usage":{"PromptTokens":4,"CompletionTokens":2,"TotalTokens":6}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"+"}}],"Created":1700549760,"Id":"148b89ef-14e1-489f-8e70-b767e5b27d56","Usage":{"PromptTokens":4,"CompletionTokens":3,"TotalTokens":7}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"1"}}],"Created":1700549760,"Id":"148b89ef-14e1-489f-8e70-b767e5b27d56","Usage":{"PromptTokens":4,"CompletionTokens":4,"TotalTokens":8}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"="}}],"Created":1700549760,"Id":"148b89ef-14e1-489f-8e70-b767e5b27d56","Usage":{"PromptTokens":4,"CompletionTokens":5,"TotalTokens":9}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"2"}}],"Created":1700549760,"Id":"148b89ef-14e1-489f-8e70-b767e5b27d56","Usage":{"PromptTokens":4,"CompletionTokens":5,"TotalTokens":9}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"stop","Delta":{"Role":"assistant","Content":""}}],"Created":1700549760,"Id":"148b89ef-14e1-489f-8e70-b767e5b27d56","Usage":{"PromptTokens":4,"CompletionTokens":5,"TotalTokens":9}}
```

**Example 4: 非流式请求成功示例**



Input: 

```
tccli hunyuan ChatStd --cli-unfold-argument  \
    --TopP 0 \
    --Stream False \
    --Temperature 0 \
    --Messages.0.Role user \
    --Messages.0.Content 你好呀！
```

Output: 
```
{
    "Note": "以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记",
    "Choices": [
        {
            "FinishReason": "stop",
            "Message": {
                "Role": "assistant",
                "Content": "你好！很高兴为您提供帮助。请问有什么问题我可以帮助您解决？"
            }
        }
    ],
    "Created": 1710902312,
    "Id": "e4657570-94a5-45f1-896c-a00ac3471d51",
    "Usage": {
        "PromptTokens": 3,
        "CompletionTokens": 14,
        "TotalTokens": 17
    }
}
```

