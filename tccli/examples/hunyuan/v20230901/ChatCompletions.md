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
    --Messages.3.Content 猫头鹰遇见眯眯眼，看得眼睛都眯成线。 \
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
    --Messages.0.Contents.2.Type image_url \
    --Messages.0.Contents.2.ImageUrl.Url https://cloudcache.tencent-cloud.com/qcloud/ui/portal-set/build/About/images/bg-product-series_87d.png \
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

**Example 10: 深度研究示例**

推荐使用 API Explorer 调用接口，见本文档顶部说明。该示例说明如何使用深度研究。

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --Model hunyuan-pro \
    --Messages.0.Role user \
    --Messages.0.Content 黄金价格为什么上涨？ \
    --Stream True \
    --StreamModeration True \
    --EnableEnhancement True \
    --SearchInfo True \
    --Citation True \
    --EnableDeepSearch True
```

Output: 
```
HTTP/1.1 200 OK
Cache-Control: no-cache
Connection: keep-alive
Content-Type: text/event-stream
Date: Wed, 23 Oct 2024 06:42:27 GMT
Transfer-Encoding: chunked
X-TC-RequestId: 962eac85-9d4d-47d5-87df-0f68e2c54ffe

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":"黄金"},"FinishReason":""}],"SearchInfo":{"SearchResults":[{"Index":1,"Title":"什么原因导致黄金价格持续上涨呢？－今日头条","Url":"https://www.toutiao.com/article/7405795153295835685/"},{"Index":2,"Title":"黄金价格上涨的背后原因－今日头条","Url":"https://www.toutiao.com/article/7343060432250749450/"},{"Index":3,"Title":"黄金为何大涨？背后的逻辑你值得深究 近一年以来，经济界 ...","Url":"https://xueqiu.com/9543769156/285918720"},{"Index":4,"Title":"金价为何猛涨u3000－u3000财梯网","Url":"https://www.cadforex.com/licai/76040.html"},{"Index":5,"Title":"黄金价格暴涨的多维驱动因素分析＿经济＿全球＿市场","Url":"https://www.sohu.com/a/792488534_121983853"},{"Index":6,"Title":"黄金价格与通货膨胀率的关联＿因素＿市场＿影响","Url":"https://www.sohu.com/a/795813780_122001933"},{"Index":7,"Title":"通货膨胀与金价的关系是怎样的？＿中金在线财经号","Url":"http://mp.cnfol.com/58227/article/1724810738-141466711.html"},{"Index":8,"Title":"金价再创新高 地缘政治和美国大选推动避险需求 - 腾讯网","Url":"https://new.qq.com/rain/a/20241023A0185900"},{"Index":9,"Title":"中信建投：通胀、货币以及地缘三大因素叠加，构成黄金完美 ...","Url":"https://new.qq.com/rain/a/20241023A01G1E00"},{"Index":10,"Title":"黄金价格与美元汇率之间的关系是怎样的－叩富网","Url":"https://licai.cofool.com/ask/qa_3396404.html"},{"Index":11,"Title":"金价暴涨释放危险信号：２０２４年，美元要崩？美债央行美元指数美元汇率黄金价格国际金价＿网易订阅","Url":"https://www.163.com/dy/article/IMSN07JG0552NMAF.html"},{"Index":12,"Title":"央行购金+投资者配置不足+地缘政治风险，金价明年将涨至 ...","Url":"https://finance.sina.com.cn/money/forex/hbfx/2024-10-23/doc-inctnyne0954128.shtml"},{"Index":13,"Title":"黄金价格与全球货币政策的互动＿市场关注＿经济＿中央银行","Url":"https://www.sohu.com/a/795813568_122001933"},{"Index":14,"Title":"黄金价格大涨，投资需求显著提升，金价还可以走多远？＿财富号＿东方财富网","Url":"https://caifuhao.eastmoney.com/news/20240306084013570039040"},{"Index":15,"Title":"国际金价再创新高！年内累计涨幅已超30%，机构称中长期 ...","Url":"https://new.qq.com/rain/a/20241018A012Y300"},{"Index":16,"Title":"从黄金历史牛市分析和预测黄金价格走势黄金＿新浪财经＿新浪网","Url":"https://finance.sina.com.cn/money/nmetal/hjzx/2024-08-20/doc-inckiaqw3372603.shtml"},{"Index":17,"Title":"以史为鉴！100年黄金走势图显示：长期策略仍是逢低买入 ...","Url":"https://finance.sina.com.cn/money/forex/hbfx/2024-02-19/doc-inaipzvn5400083.shtml"}],"Outline":["全球经济不确定性","通货膨胀预期上升","美元汇率波动","投资者需求增加","供应端因素"]},"Created":1729665576,"Id":"962eac85-9d4d-47d5-87df-0f68e2c54ffe","Usage":{"PromptTokens":6,"CompletionTokens":2,"TotalTokens":8}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":"价格"},"FinishReason":""}],"SearchInfo":{"SearchResults":[{"Index":1,"Title":"什么原因导致黄金价格持续上涨呢？－今日头条","Url":"https://www.toutiao.com/article/7405795153295835685/"},{"Index":2,"Title":"黄金价格上涨的背后原因－今日头条","Url":"https://www.toutiao.com/article/7343060432250749450/"},{"Index":3,"Title":"黄金为何大涨？背后的逻辑你值得深究 近一年以来，经济界 ...","Url":"https://xueqiu.com/9543769156/285918720"},{"Index":4,"Title":"金价为何猛涨u3000－u3000财梯网","Url":"https://www.cadforex.com/licai/76040.html"},{"Index":5,"Title":"黄金价格暴涨的多维驱动因素分析＿经济＿全球＿市场","Url":"https://www.sohu.com/a/792488534_121983853"},{"Index":6,"Title":"黄金价格与通货膨胀率的关联＿因素＿市场＿影响","Url":"https://www.sohu.com/a/795813780_122001933"},{"Index":7,"Title":"通货膨胀与金价的关系是怎样的？＿中金在线财经号","Url":"http://mp.cnfol.com/58227/article/1724810738-141466711.html"},{"Index":8,"Title":"金价再创新高 地缘政治和美国大选推动避险需求 - 腾讯网","Url":"https://new.qq.com/rain/a/20241023A0185900"},{"Index":9,"Title":"中信建投：通胀、货币以及地缘三大因素叠加，构成黄金完美 ...","Url":"https://new.qq.com/rain/a/20241023A01G1E00"},{"Index":10,"Title":"黄金价格与美元汇率之间的关系是怎样的－叩富网","Url":"https://licai.cofool.com/ask/qa_3396404.html"},{"Index":11,"Title":"金价暴涨释放危险信号：２０２４年，美元要崩？美债央行美元指数美元汇率黄金价格国际金价＿网易订阅","Url":"https://www.163.com/dy/article/IMSN07JG0552NMAF.html"},{"Index":12,"Title":"央行购金+投资者配置不足+地缘政治风险，金价明年将涨至 ...","Url":"https://finance.sina.com.cn/money/forex/hbfx/2024-10-23/doc-inctnyne0954128.shtml"},{"Index":13,"Title":"黄金价格与全球货币政策的互动＿市场关注＿经济＿中央银行","Url":"https://www.sohu.com/a/795813568_122001933"},{"Index":14,"Title":"黄金价格大涨，投资需求显著提升，金价还可以走多远？＿财富号＿东方财富网","Url":"https://caifuhao.eastmoney.com/news/20240306084013570039040"},{"Index":15,"Title":"国际金价再创新高！年内累计涨幅已超30%，机构称中长期 ...","Url":"https://new.qq.com/rain/a/20241018A012Y300"},{"Index":16,"Title":"从黄金历史牛市分析和预测黄金价格走势黄金＿新浪财经＿新浪网","Url":"https://finance.sina.com.cn/money/nmetal/hjzx/2024-08-20/doc-inckiaqw3372603.shtml"},{"Index":17,"Title":"以史为鉴！100年黄金走势图显示：长期策略仍是逢低买入 ...","Url":"https://finance.sina.com.cn/money/forex/hbfx/2024-02-19/doc-inaipzvn5400083.shtml"}],"Outline":["全球经济不确定性","通货膨胀预期上升","美元汇率波动","投资者需求增加","供应端因素"]},"Created":1729665576,"Id":"962eac85-9d4d-47d5-87df-0f68e2c54ffe","Usage":{"PromptTokens":6,"CompletionTokens":4,"TotalTokens":10}}

data: {"Note":"以上内容为AI生成，不代表开发者立场，请勿删除或修改本标记","Choices":[{"Delta":{"Role":"assistant","Content":""},"FinishReason":"stop"}],"SearchInfo":{"SearchResults":[{"Index":1,"Title":"什么原因导致黄金价格持续上涨呢？－今日头条","Url":"https://www.toutiao.com/article/7405795153295835685/"},{"Index":2,"Title":"黄金价格上涨的背后原因－今日头条","Url":"https://www.toutiao.com/article/7343060432250749450/"},{"Index":3,"Title":"黄金为何大涨？背后的逻辑你值得深究 近一年以来，经济界 ...","Url":"https://xueqiu.com/9543769156/285918720"},{"Index":4,"Title":"金价为何猛涨u3000－u3000财梯网","Url":"https://www.cadforex.com/licai/76040.html"},{"Index":5,"Title":"黄金价格暴涨的多维驱动因素分析＿经济＿全球＿市场","Url":"https://www.sohu.com/a/792488534_121983853"},{"Index":6,"Title":"黄金价格与通货膨胀率的关联＿因素＿市场＿影响","Url":"https://www.sohu.com/a/795813780_122001933"},{"Index":7,"Title":"通货膨胀与金价的关系是怎样的？＿中金在线财经号","Url":"http://mp.cnfol.com/58227/article/1724810738-141466711.html"},{"Index":8,"Title":"金价再创新高 地缘政治和美国大选推动避险需求 - 腾讯网","Url":"https://new.qq.com/rain/a/20241023A0185900"},{"Index":9,"Title":"中信建投：通胀、货币以及地缘三大因素叠加，构成黄金完美 ...","Url":"https://new.qq.com/rain/a/20241023A01G1E00"},{"Index":10,"Title":"黄金价格与美元汇率之间的关系是怎样的－叩富网","Url":"https://licai.cofool.com/ask/qa_3396404.html"},{"Index":11,"Title":"金价暴涨释放危险信号：２０２４年，美元要崩？美债央行美元指数美元汇率黄金价格国际金价＿网易订阅","Url":"https://www.163.com/dy/article/IMSN07JG0552NMAF.html"},{"Index":12,"Title":"央行购金+投资者配置不足+地缘政治风险，金价明年将涨至 ...","Url":"https://finance.sina.com.cn/money/forex/hbfx/2024-10-23/doc-inctnyne0954128.shtml"},{"Index":13,"Title":"黄金价格与全球货币政策的互动＿市场关注＿经济＿中央银行","Url":"https://www.sohu.com/a/795813568_122001933"},{"Index":14,"Title":"黄金价格大涨，投资需求显著提升，金价还可以走多远？＿财富号＿东方财富网","Url":"https://caifuhao.eastmoney.com/news/20240306084013570039040"},{"Index":15,"Title":"国际金价再创新高！年内累计涨幅已超30%，机构称中长期 ...","Url":"https://new.qq.com/rain/a/20241018A012Y300"},{"Index":16,"Title":"从黄金历史牛市分析和预测黄金价格走势黄金＿新浪财经＿新浪网","Url":"https://finance.sina.com.cn/money/nmetal/hjzx/2024-08-20/doc-inckiaqw3372603.shtml"},{"Index":17,"Title":"以史为鉴！100年黄金走势图显示：长期策略仍是逢低买入 ...","Url":"https://finance.sina.com.cn/money/forex/hbfx/2024-02-19/doc-inaipzvn5400083.shtml"},{"Index":18,"Title":"全球央行热衷“购金”！增持意愿达五年新高，高盛看涨金价至 ...","Url":"https://news.qq.com/rain/a/20240619A06NQR00"},{"Index":19,"Title":"避险地缘政治冲突，上半年全球央行增持４８３吨黄金创纪录黄金＿新浪财经＿新浪网","Url":"https://finance.sina.com.cn/jjxw/2024-08-12/doc-incikrfh1306064.shtml"},{"Index":20,"Title":"黄金热潮：央行增持背后的逻辑与投资机遇黄金价格中国人民银行＿网易订阅","Url":"https://www.163.com/dy/article/J1PCM2DH0523Q7MN.html"},{"Index":21,"Title":"金价暴涨，央行为何连续17个月增加黄金储备，后续会加仓吗","Url":"https://new.qq.com/rain/a/20240407A08EVY00"},{"Index":22,"Title":"央行增持黄金意味着什么u3000－u3000财梯网","Url":"https://www.cadforex.com/huangji/135556.html"},{"Index":23,"Title":"央行增持黄金储备如何影响黄金市场行情－指股网","Url":"https://www.zhiguf.com/focusnews_detail/1300594"},{"Index":24,"Title":"连续5个月，央行暂停增持黄金！ - 经济观察网","Url":"http://www.eeo.com.cn/2024/1020/692290.shtml"},{"Index":25,"Title":"央行，继续暂停增持黄金 - 腾讯网","Url":"https://new.qq.com/rain/a/20241007A04F7B00"},{"Index":26,"Title":"中国央行连续第五个月暂停增持黄金，分析师：空头将寻求金价跌向２６０５＿外汇动态报道＿汇通财经ｗｗｗ．ｆｘ６７８．ｃｏｍ","Url":"https://news.fx678.com/202410071146181057.shtml"},{"Index":27,"Title":"央行增持黄金意味着什么u3000－u3000财梯网","Url":"https://www.cadforex.com/huangji/135556.html"},{"Index":28,"Title":"中国央行连续15个月增持黄金，去年净购金量居全球之首","Url":"https://finance.sina.com.cn/jjxw/2024-02-07/doc-inahfexi2620119.shtml"},{"Index":29,"Title":"中国央行连续15个月增持黄金，去年净购金量居全球之首 ...","Url":"https://www.jiemian.com/article/10790382.html"},{"Index":30,"Title":"中国9月末黄金储备7280万盎司 央行连续第五个月暂停增持黄金","Url":"https://new.qq.com/rain/a/20241007A02E5O00"},{"Index":31,"Title":"１４连升！我国黄金储备２２３５．４１吨","Url":"http://www.gold.org.cn/sc1227/dzsp/202401/t20240108_195543.html"},{"Index":32,"Title":"2264.33吨！中国央行连续第5个月暂停增持黄金储备！原因为何？","Url":"https://new.qq.com/rain/a/20241007A077BF00"}],"Outline":["全球经济不确定性","通货膨胀预期上升","美元汇率波动","投资者需求增加","供应端因素"],"Mindmap":{"ThumbUrl":"https://hunyuan-plugin-nj-1258344706.cos.ap-nanjing.myqcloud.com/xmind/b70d74171af71b74a9f0b6ea2cb740e0.png","Url":"https://hunyuan-plugin-nj-1258344706.cos.ap-nanjing.myqcloud.com/xmind/b70d74171af71b74a9f0b6ea2cb740e0_t.png"},"RelevantEvents":[{"Title":"欧洲央行降息","Content":"欧洲央行在今年第三次降息，降息幅度为25个基点，全球货币环境维持宽松，为黄金的购买创造了有利环境，推动金价上涨。","Datetime":"2024-10-23","Reference":[6]},{"Title":"美元汇率走低","Content":"美元汇率走低导致美元贬值，以美元计价的黄金价格上涨。此外，全球央行净购黄金创下历史新高，进一步推动了金价上涨。","Datetime":"2024-10-13","Reference":[7,18]},{"Title":"地缘政治紧张局势","Content":"俄乌冲突、巴以冲突屡次出现升级迹象，美国大选的不确定性加剧了市场对未来全球经济增长的担忧，推动更多资金流向避险资产黄金。","Datetime":"2024-09-21","Reference":[4]},{"Title":"全球央行大量购金","Content":"近两年全球央行开始大量购金，2022年、2023年全球央行及主权机构增持黄金量均超1000吨，约占当年全球黄金产量的三分之一，导致市场供需关系变化，推高了金价。","Datetime":"2024-09-01","Reference":[2,4]},{"Title":"美联储降息预期","Content":"随着美国经济下行压力增大，市场普遍预期美联储货币政策将转向宽松周期，降息预期升温，推动黄金价格上涨。","Datetime":"2024-09-01","Reference":[2,4]}],"RelevantEntities":[{"Name":"鲍威尔[2](@ref)","Content":"美联储主席鲍威尔表示调整货币政策的时机已到，市场对于9月份美联储降息预期更为强烈，这一表态成为黄金价格上涨的重要推手。","Reference":[2]},{"Name":"特朗普[9](@ref)","Content":"特朗普当选的概率上升，市场广泛定价中期通胀中枢上移，特朗普主张的“减税+关税”政策组合导致更高的经济增长、债务增长和通胀前景，推动金价上涨。","Reference":[9]},{"Name":"国际货币基金组织[5](@ref)","Content":"国际货币基金组织长期购买黄金并保持较高储备，提升了其金融安全性，黄金成为最佳的避险资产。","Reference":[5]},{"Name":"全球央行[2,4](@ref)","Content":"近两年全球央行开始大量购金，2022年、2023年全球央行及主权机构增持黄金量均超1000吨，央行购入的黄金作为官方储备资产，推动了黄金价格的长期上涨。","Reference":[2,4]}],"Timeline":[{"Title":"现货黄金一度触及每盎司2450美元再创盘中历史新高","Url":"https://new.qq.com/rain/a/20240521A02VPJ00","Datetime":"2024-05-21 10:55:22"},{"Title":"现货黄金涨超1%至2439.19美元/盎司再度刷新历史新高","Url":"https://new.qq.com/rain/a/20240520A01GR300","Datetime":"2024-05-20 09:12:19"},{"Title":"现货黄金涨幅扩大至约1.2%重返2370美元/盎司上方","Url":"https://new.qq.com/rain/a/20240415A00H6I00","Datetime":"2024-04-15 06:42:23"},{"Title":"现货黄金首次涨穿2300美元/盎司关口","Url":"https://new.qq.com/rain/a/20240404A00BDK00","Datetime":"2024-04-04 04:48:12"},{"Title":"现货黄金盘中再创历史新高达2236美元/盎司","Url":"https://new.qq.com/rain/a/20240329A00P7I00","Datetime":"2024-03-29 07:30:14"},{"Title":"国内黄金首饰价格突破645元/克","Url":"https://new.qq.com/rain/a/20240305A096Z000","Datetime":"2024-03-05 20:06:29"},{"Title":"纽约金价首次收盘站上2100美元","Url":"https://new.qq.com/rain/a/20240305A01GFM00","Datetime":"2024-03-05 09:18:26"},{"Title":"CFTC数据显示黄金看涨情绪创三周新高","Url":"https://new.qq.com/rain/a/20240302A00ISM00","Datetime":"2024-03-02 04:48:30"}]},"Created":1729665606,"Id":"962eac85-9d4d-47d5-87df-0f68e2c54ffe","Usage":{"PromptTokens":6,"CompletionTokens":2068,"TotalTokens":2074}}
```

