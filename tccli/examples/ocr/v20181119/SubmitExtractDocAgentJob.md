**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli ocr SubmitExtractDocAgentJob --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --ItemNames.0.KeyName 车辆牌号 \
    --ItemNames.0.KeyPrompt 车辆牌号 \
    --ItemNames.1.KeyName 卸货地点 \
    --ItemNames.2.KeyName 铅封号
```

Output: 
```
{
    "Response": {
        "JobId": "1337031538243026944",
        "RequestId": "03ceea30-689d-4897-b3f6-719105213526"
    }
}
```

**Example 2: 调用成功示例2**

调用成功示例2

Input: 

```
tccli ocr SubmitExtractDocAgentJob --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --ItemNames.0.KeyName 项目 \
    --ItemNames.0.KeyType 1 \
    --ItemNames.1.KeyName 费用名称 \
    --ItemNames.1.KeyType 1 \
    --ItemNames.1.KeyPrompt 相近词：人民币 \
    --ItemNames.2.KeyName 美金 \
    --ItemNames.2.KeyType 1 \
    --ItemNames.3.KeyName 欧元 \
    --ItemNames.3.KeyType 1 \
    --ItemNames.4.KeyName 开航日 \
    --ItemNames.4.KeyType 0
```

Output: 
```
{
    "Response": {
        "JobId": "1337322230114697216",
        "RequestId": "2659e485-d475-471f-9efa-c94f3f7a8e11"
    }
}
```

