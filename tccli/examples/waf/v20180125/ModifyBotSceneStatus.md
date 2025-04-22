**Example 1: test**



Input: 

```
tccli waf ModifyBotSceneStatus --cli-unfold-argument  \
    --Status false \
    --SceneId 3000004869 \
    --Domain fgsta.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "RequestId": "a76b75a1-26d0-4968-a4c3-64cd06444fa4"
    }
}
```

**Example 2: BOT全局总开关**



Input: 

```
tccli waf ModifyBotSceneStatus --cli-unfold-argument  \
    --Domain test.com \
    --SceneId 30xxxxxxx \
    --Status False
```

Output: 
```
{
    "Response": {
        "RequestId": "a0b4e55b-5307-4378-856d-efc22475c77d"
    }
}
```

