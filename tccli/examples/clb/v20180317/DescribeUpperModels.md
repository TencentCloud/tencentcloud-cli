**Example 1: 查询上游模型列表**



Input: 

```
tccli clb DescribeUpperModels --cli-unfold-argument  \
    --ApiKey sk-xxx \
    --ApiBase http://11.141.93.233/v1 \
    --AccessType PublicBYOK \
    --ModelProvider openai
```

Output: 
```
{
    "Response": {
        "Models": [
            "gpt-4o"
        ],
        "RequestId": "21038259-1326-4b35-92f9-b44e77cf25db"
    }
}
```

