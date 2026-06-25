**Example 1: 示例**

示例

Input: 

```
tccli dataagent AppendKnowledgeTask --cli-unfold-argument  \
    --InstanceId dataagent-haBKQxLt \
    --KnowledgeBaseId klbase-YuVJ1k3U37 \
    --FileId 2ca9279d-21ea-4e39-8b3b-c49c65ba83eb \
    --Documents.0.FileName test.csv \
    --Documents.0.FileId 2ca9279d-21ea-4e39-8b3b-c49c65ba83ea \
    --Documents.0.FileUrl https://data-agent-dev-1353879163.cos.ap-chongqing.myqcloud.com/user-storage/100041873387/klbase-YuVJ1k3U37/2ca9279d-21ea-4e39-8b3b-c49c65ba83eb_test.csv \
    --Documents.0.FileSize 111111
```

Output: 
```
{
    "Response": {
        "RequestId": "4ba63c62-7da8-4715-807c-a7fb4ddf81cd"
    }
}
```

