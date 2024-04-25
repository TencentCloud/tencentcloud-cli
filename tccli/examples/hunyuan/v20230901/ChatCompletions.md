**Example 1: system参数示例**

system提示词

Input: 

```
tccli hunyuan ChatCompletions --cli-unfold-argument  \
    --TopP 1 \
    --Temperature 1 \
    --Model hunyuan-lite \
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

