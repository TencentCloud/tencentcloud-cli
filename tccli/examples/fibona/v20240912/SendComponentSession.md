**Example 1: 成功调用**

调用成功

Input: 

```
tccli fibona SendComponentSession --cli-unfold-argument  \
    --UserGroupUniqueID rum-qZsJlN6****5QJEO** \
    --SessionID 411 \
    --Clues {"你好":[{"tag":"chat","content":"你好"}]}
```

Output: 
```
data: {"code":0,"data":{"action":"desensitization","finished":false,"meta_data":{"content":"null"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"d27a7b48-e0eb-4992-8879-f01742d885c0","name":"root","action":"root:start","finished":false,"meta_data":{}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:start","finished":false,"meta_data":{}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好","delta":"您好"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！","delta":"！"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您","delta":"如果您"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何","delta":"有任何"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题","delta":"问题"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或","delta":"或"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要","delta":"想要"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论","delta":"讨论"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题","delta":"的话题"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请","delta":"，请"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时","delta":"随时"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我","delta":"告诉我"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我。","delta":"。"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我。我很","delta":"我很"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我。我很乐意","delta":"乐意"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我。我很乐意为您提供","delta":"为您提供"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我。我很乐意为您提供帮助","delta":"帮助"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:streaming","finished":false,"meta_data":{"content":"您好！如果您有任何问题或想要讨论的话题，请随时告诉我。我很乐意为您提供帮助。","delta":"。"}},"msg":"success"}

data: {"code":0,"data":{"res_id":"9df902e5-97c1-4e50-a02c-c2dbc64ea92d","name":"hunyuan","action":"llm:end","finished":false,"meta_data":{}},"msg":"success"}

data: {"code":0,"data":{"action":"full_texts","finished":false,"meta_data":{"full_texts":["您好！如果您有任何问题或想要讨论的话题，请随时告诉我。我很乐意为您提供帮助。"]}},"msg":"success"}

data: {"code":0,"data":{"action":"msg_ids","finished":false,"meta_data":{"ids":[7471,7472]}},"msg":"success"}

data: {"code":0,"data":{"action":"token_num","finished":false,"meta_data":{"token_num":[0,0]}},"msg":"success"}

data: {"code":0,"data":{"action":"root:done","finished":true,"meta_data":{}},"msg":"success"}


```

**Example 2: 进行会话**

会话

Input: 

```
tccli fibona SendComponentSession --cli-unfold-argument  \
    --UserGroupUniqueID rum-M2seOxn4Cn4YlQVMp \
    --SessionID 619 \
    --Clues {"崩溃设备信息":[{"content":"机型：ALN-AL80(proportion:100%)\n      应用类型(开发平台)：harmonyos(proportion:100%)\n      CPU架构：arm64-v8a(proportion:100%)\n      系统版本：OpenHarmony-5.0.1.73(Beta1)(proportion:100%)\n      崩溃时应用在前/后台：foreground(proportion:100%) \n      "}],"崩溃问题原因":[{"content":"native_crash | signal 11(SIGSEGV), code 1(SEGV_MAPERR), address 0x0000000000000100"}],"崩溃线程堆栈":[{"content":"000000000000617c /data/storage/el1/bundle/libs/arm64/"}]}
```

Output: 
```
{
    "code": 0,
    "data": {
        "action": "root:done",
        "finished": true,
        "meta_data": {}
    },
    "msg": "success"
}
```

