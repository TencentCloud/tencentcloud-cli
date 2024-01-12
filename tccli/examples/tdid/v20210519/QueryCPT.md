**Example 1: 查询凭证模板内容**

根据凭证模板ID查询凭证模板内容

Input: 

```
tccli tdid QueryCPT --cli-unfold-argument  \
    --DAPId 1 \
    --CPTId 1001
```

Output: 
```
{
    "Response": {
        "CPTJson": "{\n  \"CPTType\" : \"original\",\n  \"$schema\" : \"http://json-schema.org/draft-04/schema#\",\n  \"description\" : \"RevertBill\",\n  \"title\" : \"RevertBill\",\n  \"type\" : \"object\",\n  \"properties\" : {\n    \"transferOutEntDid\" : {\n      \"description\" : \"transferOutEntDid\",\n      \"type\" : \"string\"\n    }\n  },\n  \"required\" : [ \"transferOutEntDid\" ]\n}",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

