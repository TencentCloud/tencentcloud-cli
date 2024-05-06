**Example 1: system参数示例**

system提示词

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-pro \
    --Messages.0.Role system \
    --Messages.0.Content 将英文单词转换为包括中文翻译、英文释义和一个例句的完整解释。请检查所有信息是否准确，并在回答时保持简洁，不需要任何其他反馈。 \
    --Messages.1.Role user \
    --Messages.1.Content nice
```

Output: 
```
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"很好"}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":1,"TotalTokens":37}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"："}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":2,"TotalTokens":38}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"nice"}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":3,"TotalTokens":39}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"\n"}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":4,"TotalTokens":40}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"英文"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":5,"TotalTokens":41}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"释义"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":6,"TotalTokens":42}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"："}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":7,"TotalTokens":43}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"ple"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":8,"TotalTokens":44}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"asing"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":9,"TotalTokens":45}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" or"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":10,"TotalTokens":46}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" acceptable"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":11,"TotalTokens":47}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"\n"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":12,"TotalTokens":48}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"例"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":13,"TotalTokens":49}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"句"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":14,"TotalTokens":50}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"："}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":15,"TotalTokens":51}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"She"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":16,"TotalTokens":52}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" had"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":17,"TotalTokens":53}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" a"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":18,"TotalTokens":54}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" nice"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":19,"TotalTokens":55}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" smile"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":20,"TotalTokens":56}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"."}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":21,"TotalTokens":57}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"stop","Delta":{"Role":"assistant","Content":""}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":21,"TotalTokens":57}}
```

**Example 2: 多轮对话示例**

多轮对话场景

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-pro \
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
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"青蛙"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":1,"TotalTokens":86}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"跳"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":2,"TotalTokens":87}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"高"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":3,"TotalTokens":88}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"，"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":4,"TotalTokens":89}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"比"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":5,"TotalTokens":90}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"下马"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":6,"TotalTokens":91}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"。"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":7,"TotalTokens":92}}
{"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"stop","Delta":{"Role":"assistant","Content":""}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":7,"TotalTokens":92}}
```

**Example 3: 请求失败示例**



Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 0 \
    --Temperature 4.8 \
    --Model hunyuan-pro \
    --Messages.0.Role user \
    --Messages.0.Content 介绍下自己
```

Output: 
```
{
    "Response": {
        "RequestId": "188cc996-ab09-49a7-aa9f-1df88f11c6b4",
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Temperature must be 2 or less"
        }
    }
}
```

**Example 4: 流式请求成功示例**



Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-pro \
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

**Example 5: 非流式请求成功示例**



Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 0 \
    --Stream False \
    --Temperature 0 \
    --Model hunyuan-pro \
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

