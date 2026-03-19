**Example 1: 修改已有模板**



Input: 

```
tccli vod ModifyLLMComprehendTemplate --cli-unfold-argument  \
    --Definition 100002 \
    --SubAppId 220885 \
    --Model Basic \
    --Summary.Switch OFF \
    --Summary.ExtendedParameter  \
    --Asr.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "0b6c7338-2dae-4454-a91b-1bdc219c5b9f"
    }
}
```

