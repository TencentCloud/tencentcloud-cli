**Example 1: 批量修改问答适用范围**



Input: 

```
tccli lke ModifyQAAttrRange --cli-unfold-argument  \
    --BotBizId 1742501052613230592 \
    --QaBizIds 1762058568200880128 \
    --AttrLabels.0.AttributeBizId 1759039436899221504 \
    --AttrLabels.0.Source 1 \
    --AttrLabels.0.LabelBizIds 1759039436924387328 \
    --AttrRange 2
```

Output: 
```
{
    "Response": {
        "RequestId": "9a81d98f-5fea-450f-8d8d-0ba8a985972f"
    }
}
```

