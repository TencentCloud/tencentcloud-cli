**Example 1: system prompt 示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明 system prompt 的使用方法。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-pro \
    --Stream True \
    --Messages.0.Role system \
    --Messages.0.Content 将英文单词转换为包括中文翻译、英文释义和一个例句的完整解释。请检查所有信息是否准确，并在回答时保持简洁，不需要任何其他反馈。 \
    --Messages.1.Role user \
    --Messages.1.Content nice
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

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"很好"}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":1,"TotalTokens":37}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"："}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":2,"TotalTokens":38}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"nice"}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":3,"TotalTokens":39}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"\n"}}],"Created":1705634813,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":4,"TotalTokens":40}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"英文"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":5,"TotalTokens":41}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"释义"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":6,"TotalTokens":42}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"："}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":7,"TotalTokens":43}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"ple"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":8,"TotalTokens":44}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"asing"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":9,"TotalTokens":45}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" or"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":10,"TotalTokens":46}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" acceptable"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":11,"TotalTokens":47}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"\n"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":12,"TotalTokens":48}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"例"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":13,"TotalTokens":49}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"句"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":14,"TotalTokens":50}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"："}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":15,"TotalTokens":51}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"She"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":16,"TotalTokens":52}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" had"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":17,"TotalTokens":53}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" a"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":18,"TotalTokens":54}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" nice"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":19,"TotalTokens":55}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":" smile"}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":20,"TotalTokens":56}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"."}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":21,"TotalTokens":57}}
	
data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"stop","Delta":{"Role":"assistant","Content":""}}],"Created":1705634814,"Id":"681ef57e-9f1e-4faa-a2d3-07b655a1fa1f","Usage":{"PromptTokens":36,"CompletionTokens":21,"TotalTokens":57}}
```

**Example 2: 多轮对话示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明如何给模型传入多轮消息。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-pro \
    --Stream True \
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
HTTP/1.1 200 OK
Cache-Control: no-cache
Connection: keep-alive
Content-Type: text/event-stream
Date: Tue, 21 Nov 2023 06:56:00 GMT
Transfer-Encoding: chunked
X-TC-RequestId: 61a8459b-27c8-4868-af8f-f374db0245f8

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"青蛙"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":1,"TotalTokens":86}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"跳"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":2,"TotalTokens":87}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"高"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":3,"TotalTokens":88}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"，"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":4,"TotalTokens":89}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"比"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":5,"TotalTokens":90}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"下马"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":6,"TotalTokens":91}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"","Delta":{"Role":"assistant","Content":"。"}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":7,"TotalTokens":92}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"FinishReason":"stop","Delta":{"Role":"assistant","Content":""}}],"Created":1705634032,"Id":"9c772634-8824-43e8-bc24-8bc4c19b9151","Usage":{"PromptTokens":85,"CompletionTokens":7,"TotalTokens":92}}
```

**Example 3: 请求失败示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例给出接口调用失败时的响应例子。

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

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例给出接口正常调用时的响应例子。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-pro \
    --Stream True \
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

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明如何用非流式方式调用接口。

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

**Example 6: hunyuan-functioncall模型非流式请求成功示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明hunyuan-functioncall模型如何用非流式方式调用接口。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 0 \
    --Stream False \
    --Temperature 0 \
    --Model hunyuan-functioncall \
    --Messages.0.Role user \
    --Messages.0.Content 北京和深圳今天天气如何 \
    --Tools.0.Type function \
    --Tools.0.Function.Name get_current_weather \
    --Tools.0.Function.Description 获取当前地点的天气 \
    --Tools.0.Function.Parameters {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "城市名称"
                        },
                        "unit": {
                            "type": "string",
                            "enum": [
                                "celsius",
                                "fahrenheit"
                            ]
                        }
                    },
                    "required": [
                        "location"
                    ]
                } \
    --ToolChoice auto
```

Output: 
```
{
    "Response": {
        "RequestId": "e7f5ce41-87fd-4977-803c-54cded687cd9",
        "Note": "以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记",
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "使用get_current_weather工具来获取北京和深圳的当前天气情况。\n\t\n\t用户想要知道北京和深圳今天的天气情况。用户的请求是关于天气的查询，需要使用天气查询工具来获取信息。",
                    "ToolCalls": [
                        {
                            "Type": "function",
                            "Function": {
                                "Name": "get_current_weather",
                                "Arguments": "{\"location\":[\"北京\",\"深圳\"],\"unit\":\"celsius\"}"
                            }
                        }
                    ]
                },
                "FinishReason": "tool_calls"
            }
        ],
        "Created": 1719638614,
        "Usage": {
            "PromptTokens": 6,
            "CompletionTokens": 46,
            "TotalTokens": 52
        }
    }
}
```

**Example 7: hunyuan-functioncall模型流式请求成功示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明hunyuan-functioncall模型如何用流式方式调用接口。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --Model hunyuan-functioncall \
    --Stream True \
    --Messages.0.Role user \
    --Messages.0.Content 北京和深圳今天天气如何 \
    --Tools.0.Type function \
    --Tools.0.Function.Name get_current_weather \
    --Tools.0.Function.Description 获取当前地点的天气 \
    --Tools.0.Function.Parameters {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "城市名称"
                        },
                        "unit": {
                            "type": "string",
                            "enum": [
                                "celsius",
                                "fahrenheit"
                            ]
                        }
                    },
                    "required": [
                        "location"
                    ]
                } \
    --ToolChoice auto
```

Output: 
```
说明：  对于Delta.ToolCalls每一次的输出值应该以Id为标识对Type、Name、Arguments字段进行合并，本示例中的ToolCalls 最终值为：[{"Id": "call_cq177uk2c3m1v7ep35dg","Type": "function","Function": {"Name": "get_current_weather", "Arguments": "{\"location\":[\"北京\",\"深圳\"],\"unit\":\"celsius\"}"}}]

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":"","ToolCalls":[{"Id":"call_cq154vk2c3m1v7ep3530","Type":"function","Function":{"Name":"get_current_weather","Arguments":""}}]},"FinishReason":""}],"Created":1719816830,"Id":"cd37cf66-089f-4ab2-8118-e18baa238462","Usage":{"PromptTokens":6,"CompletionTokens":0,"TotalTokens":6}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":"","ToolCalls":[{"Id":"call_cq154vk2c3m1v7ep3530","Type":"function","Function":{"Name":"","Arguments":"{\"location\":\"北京\"}"}}]},"FinishReason":""}],"Created":1719816830,"Id":"cd37cf66-089f-4ab2-8118-e18baa238462","Usage":{"PromptTokens":6,"CompletionTokens":0,"TotalTokens":6}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":"计划使用get_current_weather工具来获取北京和深圳的当前天气。\n\t\n\t用户想要知道北京和深圳今天的天气情况。用户的请求是关于天气的查询，需要使用天气查询工具来获取信息。"},"FinishReason":""}],"Created":1719816830,"Id":"cd37cf66-089f-4ab2-8118-e18baa238462","Usage":{"PromptTokens":6,"CompletionTokens":46,"TotalTokens":52}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":""},"FinishReason":"tool_calls"}],"Created":1719816830,"Id":"cd37cf66-089f-4ab2-8118-e18baa238462","Usage":{"PromptTokens":6,"CompletionTokens":46,"TotalTokens":52}}
```

**Example 8: hunyuan-functioncall模型多轮对话示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明hunyuan-functioncall模型多轮对话如何调用接口。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --Model hunyuan-functioncall \
    --Messages.0.Role user \
    --Messages.0.Content 北京和深圳今天天气如何 \
    --Messages.1.Role assistant \
    --Messages.1.Content 使用get_current_weather工具来获取北京和深圳的当前天气。
	
	用户想要知道北京和深圳今天的天气情况。用户提供了两个城市名称，但没有指定温度单位，根据常识，默认用户需要的是摄氏度。 \
    --Messages.1.ToolCalls.0.Id call_cq16e7k2c3m1v7ep35c0 \
    --Messages.1.ToolCalls.0.Type function \
    --Messages.1.ToolCalls.0.Function.Name get_current_weather \
    --Messages.1.ToolCalls.0.Function.Arguments {"location":"北京","unit":"celsius"} \
    --Messages.2.Role tool \
    --Messages.2.ToolCallId call_cq16e7k2c3m1v7ep35c0 \
    --Messages.2.Content {"temperature": 35, "wind": "南", "condition": "暴雨"} \
    --Tools.0.Type function \
    --Tools.0.Function.Name get_current_weather \
    --Tools.0.Function.Description 获取当前地点的天气 \
    --Tools.0.Function.Parameters {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "城市名称"
                        },
                        "unit": {
                            "type": "string",
                            "enum": [
                                "celsius",
                                "fahrenheit"
                            ]
                        }
                    },
                    "required": [
                        "location"
                    ]
                } \
    --ToolChoice auto
```

Output: 
```
{
    "Response": {
        "RequestId": "5a112898-d802-4bca-8ba2-7ce2388b98e8",
        "Note": "以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记",
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "北京今天的天气情况是：\n温度：35摄氏度\n风向：南\n天气状况：暴雨\n\n深圳今天的天气情况是：\n温度：35摄氏度\n风向：南\n天气状况：暴雨"
                },
                "FinishReason": "stop"
            }
        ],
        "Created": 1719822322,
        "Id": "5a112898-d802-4bca-8ba2-7ce2388b98e8",
        "Usage": {
            "PromptTokens": 71,
            "CompletionTokens": 42,
            "TotalTokens": 113
        }
    }
}
```

**Example 9: 图片理解示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明hunyuan-vision模型如何调用接口。

ImageUrl.Url 支持图片链接以及图片 base64 两种方式
jpeg 图片转 base64 示例 (其他图片格式注意修改为对应的 MIME 类型, 如 image/png, image/webp, image/bmp 等):

```python
import base64

with open("1.jpeg", 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read())
    print("data:image/jpeg;base64,"+encoded_image.decode('utf-8'))
```

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --Model hunyuan-vision \
    --Messages.0.Role user \
    --Messages.0.Contents.0.Type text \
    --Messages.0.Contents.0.Text 下面图片中是哪个公司的 Logo？ \
    --Messages.0.Contents.1.Type image_url \
    --Messages.0.Contents.1.ImageUrl.Url https://cloudcache.tencent-cloud.com/qcloud/ui/portal-set/build/About/images/bg-product-series_87d.png \
    --Stream False
```

Output: 
```
{
    "Response": {
        "RequestId": "a21f9d7e-c18a-438b-bfb4-7941a2adf8ae",
        "Note": "以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记",
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "这张图片中展示的Logo属于腾讯公司。"
                },
                "FinishReason": "stop"
            }
        ],
        "Created": 1714290436,
        "Id": "a21f9d7e-c18a-438b-bfb4-7941a2adf8ae",
        "Usage": {
            "PromptTokens": 7,
            "CompletionTokens": 10,
            "TotalTokens": 17
        }
    }
}
```

