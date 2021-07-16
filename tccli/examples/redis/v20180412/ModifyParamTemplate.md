**Example 1: 请求示例**



Input: 

```
tccli redis ModifyParamTemplate --cli-unfold-argument  \
    --ParamList.0.Value 120 \
    --ParamList.0.Key timeout \
    --TemplateId crs-cfg-sa23d5d3 \
    --Description MyCustomParamTemplate \
    --Name CustomParamTemplate
```

Output: 
```
{
    "Response": {
        "RequestId": "0e728fa9-c2e5-4bf8-8d6b-c1c4fab7b6db"
    }
}
```

