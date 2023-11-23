**Example 1: 请求失败示例**



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

**Example 2: 请求成功示例**



Input: 

```
tccli hunyuan ChatStd --cli-unfold-argument  \
    --TopP 0 \
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

