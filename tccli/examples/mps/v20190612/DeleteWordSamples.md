**Example 1: 示例**

一个删除关键词样本示例请求

Input: 

```
tccli mps DeleteWordSamples --cli-unfold-argument  \
    --Keywords abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 删除关键词样本**

一个示例请求

Input: 

```
tccli mps DeleteWordSamples --cli-unfold-argument  \
    --Keywords 张三
```

Output: 
```
{
    "Response": {
        "RequestId": "510f4d68-09c9-44a3-ab55-192ff22297c9"
    }
}
```

