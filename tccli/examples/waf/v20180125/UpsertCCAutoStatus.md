**Example 1: Waf 斯巴达版本更新cc自动封堵状态**



Input: 

```
tccli waf UpsertCCAutoStatus --cli-unfold-argument  \
    --Domain test.com \
    --Value 1
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "a0b4e55b-5307-4378-856d-efc22475c77d"
    }
}
```

