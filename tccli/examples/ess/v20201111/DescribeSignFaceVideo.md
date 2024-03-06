**Example 1: 查询签署认证人脸视频结果**

1. 个人用户在H5端完成合同签署，通过视频问答模式认证。
2. 所需白名单已经开通。
3. 在签署完成后的三天内获取人脸图片。

Input: 

```
tccli ess DescribeSignFaceVideo --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --SignId yDCNOUUckpv3ecwcUECtq4n1jXPLxLq7
```

Output: 
```
{
    "Response": {
        "IntentionQuestionResult": {
            "AsrResult": [
                "同意"
            ],
            "ResultCode": [
                "0"
            ],
            "Video": "AAAAHGZ0eXBpc281AAAAAWlzb21pc281aGxzZgAAB"
        },
        "RequestId": "s1709628366717791449",
        "VideoData": {
            "LiveNessVideo": "AAAAHGZ0eXBpc281AAAAAWlzb21pc281aGxzZgAAB"
        }
    }
}
```

