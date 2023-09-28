**Example 1: 创建企业信息变更链接**

设置changeType为2，创建企业信息变更链接。

Input: 

```
tccli essbasic CreateChannelOrganizationInfoChangeUrl --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "38be082e-08c4-4f37-a0b7-cd47cf9982b5"
    }
}
```

**Example 2: 创建超管变更链接**

设置changeType为1，创建企业超管变更链接

Input: 

```
tccli essbasic CreateChannelOrganizationInfoChangeUrl --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3bff7e92-76f8-4e09-85df-e7cb982cb454"
    }
}
```

**Example 3: 错误示例-变更类型不合法**

设置changeType为3，接口将返回错误信息。

Input: 

```
tccli essbasic CreateChannelOrganizationInfoChangeUrl --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "不支持的变更类型:3,请确认后重新"
        },
        "RequestId": "30cc3f4a-8f8c-4ec7-a6fb-66a82590c546"
    }
}
```

