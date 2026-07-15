**Example 1: 创建BYOK模型**



Input: 

```
tccli clb CreateModel --cli-unfold-argument  \
    --AccessType PrivateCustom \
    --ModelIds.0.ModelId gpt-4o \
    --ModelIds.0.ModelAlias 2rasd \
    --Keys.0.ApiKey sk-test-openai-key-003 \
    --Keys.0.Name test-key-5 \
    --ModelProvider openai \
    --ServiceProviderName custom \
    --ApiBase http://127.0.0.1:8080 \
    --VpcId vpc-j5bxoqef \
    --SubnetId subnet-60enc8ny \
    --HostHeader www.a.com \
    --Tags.0.TagKey ekkocao \
    --Tags.0.TagValue t3
```

Output: 
```
{
    "Response": {
        "KeyIds": [
            "mkey-ec5ukd0r"
        ],
        "ServiceProviderId": "byok-d4yf0jkd",
        "RequestId": "65f4eb1b-14a8-401a-86c3-3394d1ee96cd"
    }
}
```

**Example 2: 创建仅支持文本输入的byok实例**

创建仅支持文本输入的byok实例

Input: 

```
tccli clb CreateModel --cli-unfold-argument  \
    --AccessType PublicCustom \
    --ModelProvider openai \
    --ModelIds.0.ModelId gpt-4o \
    --ModelIds.0.ModelAlias my-gpt-4o \
    --ModelIds.0.InputModalities text \
    --Keys.0.ApiKey sk-111111111 \
    --Keys.0.Name sk-1 \
    --ApiBase http://11.141.93.26:10000/v1 \
    --Tags.0.TagKey text \
    --Tags.0.TagValue text
```

Output: 
```
{
    "Response": {
        "KeyIds": [
            "mkey-qd6kwrnt"
        ],
        "ServiceProviderId": "byok-lfwolo91",
        "RequestId": "ff11ef23-44dc-45d5-88d2-5ca2f2338380"
    }
}
```

