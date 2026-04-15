**Example 1: 智能生成检索语句-不开启深度思考-流式调用**

此示例说明如何通过流式调用接口，以及如何传递历史上下文会话内容。注意：流式调用的请求域名，请务必配置为 cls.ai.tencentcloudapi.com (VPC内网环境可配置 cls.ai.internal.tencentcloudapi.com）。

Input: 

```
tccli cls ChatCompletions --cli-unfold-argument  \
    --Model text2sql \
    --Messages.0.Role user \
    --Messages.0.Content 状态码200, 统计日志条数 \
    --Messages.1.Role assistant \
    --Messages.1.Content 根据您的需求"状态码200, 统计日志条数"，我分析出这是一个检索分析需求，需要检索状态码为200的日志，并统计日志条数。

根据Nginx日志主题的字段配置，`status`字段是long类型且开启了统计状态。以下是生成的CQL语句：

\`\`\`sql
status:200 | SELECT count(*) AS log_count
\`\`\`

**解释说明：**
1. **检索条件**：`status:200` - 检索状态码为200的日志
2. **SQL语句**：`SELECT count(*) AS log_count` - 统计符合条件的日志条数
3. **校验结果**：校验语句通过

由于这是一个统计查询，需要使用管道符`|`将检索条件和SQL分析语句连接起来。语句使用了`status:200`作为检索条件，然后通过`count(*)`函数统计日志条数。 \
    --Messages.2.Content 再统计5xx的 \
    --Messages.2.Role user \
    --Stream True \
    --Metadata.0.Key topic_id \
    --Metadata.0.Value xxxxxxxx-xxxx \
    --Metadata.1.Key topic_region \
    --Metadata.1.Value ap-guangzhou
```

Output: 
```
id: 1
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"根据","Role":"assistant","ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103178,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 2
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"您的需求\"","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103178,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 3
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"再统计5","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103178,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 4
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"xx的\"，","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103178,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 5
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"这是","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 6
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"要","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 7
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"统计HTTP","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 8
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"状态码为","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 9
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"5xx（","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 10
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"服务器错误）","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 11
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"的日志条","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 12
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"数。\n\n","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 13
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"根据日志主题","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 14
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"字段","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 15
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"列表，`","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 16
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"status`","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 17
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"字段是long","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 18
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"类型且开启了","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 19
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"统计状态。","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 20
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"以下是生成的","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 21
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"CQL语句","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 22
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"：\n\n\`\`\`sql","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 23
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"\nstatus","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 24
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":">=500 AND","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 25
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" status<=","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 26
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"599 |","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 27
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" SELECT count(*)","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 28
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" AS log","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 29
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"_count\n\`\`\`\n\n","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 30
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"**解释说明","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 31
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"：**\n1","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 32
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":". **检索","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103179,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 33
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"条件**：","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 34
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"`status>=","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 35
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"500 AND status","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 36
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"<=599`","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 37
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" - 检索","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 38
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"状态码在","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 39
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"500-","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 40
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"599之间的","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 41
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"日志（5","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 42
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"xx服务器","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 43
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"错误）\n2","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 44
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":". **","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 45
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"SQL语句**","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 46
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"：`SELECT","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 47
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" count(*) AS","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 48
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" log_count`","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 49
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":" - 统计","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 50
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"符合条件的日志条","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 51
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"数\n3","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 52
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":". **校验","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 53
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"结果**：","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 54
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"校验语句","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 55
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"通过\n\n","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 56
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"该","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 57
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"语句使用了","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 58
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"数值","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 59
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"范围检索","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 60
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"条件","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103180,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 61
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"`status>=","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 62
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"500 AND status","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 63
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"<=599`","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 64
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"来匹配","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 65
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"所有","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 66
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"5xx状态","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 67
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"码，","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 68
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"然后统计","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 69
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"满足","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 70
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"条件的日志数量","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 71
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":"。","Role":null,"ReasoningContent":null},"Index":0,"FinishReason":null}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{}}

id: 72
data: {"RequestId":"xxxxxxxx-xxxx","Id":"xxxxxxxx-xxxx","Choices":[{"Delta":{"Content":null,"Role":null,"ReasoningContent":null},"Index":0,"FinishReason":"stop"}],"Created":1775103181,"Model":"text2sql","Object":"chat.completion.chunk","Usage":{"PromptTokens":12482,"CompletionTokens":175,"TotalTokens":12657}}
```

**Example 2: 智能生成检索语句-开启深度思考-非流式调用**

此示例说明如何通过非流式调用接口。

Input: 

```
tccli cls ChatCompletions --cli-unfold-argument  \
    --Messages.0.Content 状态码200, 统计日志条数 \
    --Messages.0.Role user \
    --Model text2sql-reasoning \
    --Metadata.0.Key topic_region \
    --Metadata.0.Value ap-guangzhou \
    --Metadata.1.Key topic_id \
    --Metadata.1.Value xxxxxxxx-xxxx
```

Output: 
```
{
  "Response": {
    "RequestId": "xxxxxxxx-xxxx",
    "Id": "xxxxxxxx-xxxx",
    "Created": 1775102996,
    "Model": "text2sql-reasoning",
    "Choices": [
      {
        "FinishReason": "stop",
        "Message": {
          "Role": "assistant",
          "Content": "\n\`\`\`sql\nstatus:200 | SELECT count(*) AS \"日志条数\"\n\`\`\`\n\n### 解释说明：\n1. **检索条件**：`status:200`\n   - 使用键值检索语法过滤状态码为200的日志\n   - `status`字段在索引配置中已开启统计（状态为1），可直接使用\n\n2. **分析语句**：`SELECT count(*) AS \"日志条数\"`\n   - 使用聚合函数`count(*)`统计符合条件的日志条数\n   - 字段别名使用双引号包裹（包含中文）\n\n3. **注意事项**：\n   - 该语句统计的是当前查询时间范围内的日志条数\n   - 如需调整时间范围，请在控制台右侧时间选择器修改\n   - `status`字段为long类型，支持精确数值检索\n\n### 校验结果：\n\`\`\`json\n{\n  \"status\": \"success\",\n  \"result\": {\n    \"日志条数\": 15234\n  }\n}\n\`\`\`",
          "ReasoningContent": "\n我们已知日志主题索引配置字段列表，其中包含字段：status:long::1，表示status字段是long类型，开启统计。\n 需求是：状态码200, 统计日志条数。\n 根据规则，纯统计需求应使用检索分析格式：[检索条件] | [SQL语句]\n 检索条件：状态码200，即status:200\n SQL语句：统计日志条数，即SELECT count(*) AS log_count\n\n 注意：由于status字段在索引配置中已开启统计，可以直接使用。\n\n 输出CQL语句：`status:200 | SELECT count(*) AS log_count`\n\n 解释说明：检索条件为status:200，然后使用SQL统计日志条数。\n\n 另外，由于需求中指定了状态码200，我们不需要考虑时间范围，因为用户可以在界面选择时间范围。\n\n 校验：我们可以模拟校验，假设有status字段且值为200的日志，则统计其数量。如果日志中没有status字段或没有值为200的日志，则返回0。\n\n 由于我们使用了已开启统计的字段，所以不会出现字段未开启统计的问题。\n\n 因此，最终输出如下：",
          "ToolCalls": []
        },
        "Index": 0
      }
    ],
    "Usage": {
      "PromptTokens": 11262,
      "CompletionTokens": 448,
      "TotalTokens": 11710
    }
  }
}
```

